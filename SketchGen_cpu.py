from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from sketchui import Ui_SketchGen
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem, QGraphicsView, QGraphicsItem, QColorDialog, QGraphicsView

import cv2 as cv
import sys, os, subprocess, string

import torch
from torchvision import transforms
from torchvision.utils import save_image
from torch.utils.serialization import load_lua

from PIL import Image

class MainWindowUI(QtWidgets.QMainWindow, Ui_SketchGen):

    def __init__(self):
        super(MainWindowUI, self).__init__()
        self.setupUi(self)
        self._translate = QtCore.QCoreApplication.translate
        self.show()

        self.actionOpen.triggered.connect(self.openImage)
        self.openButton.clicked.connect(self.openImage)

        self.actionSketch.triggered.connect(self.sketchImage)
        self.sketchButton.clicked.connect(self.sketchImage)

        self.actionSave.triggered.connect(self.saveImage)
        self.saveButton.clicked.connect(self.saveImage)

        self.actionQuit.triggered.connect(self.exitApp)
        app.aboutToQuit.connect(self.exitApp)


    def openImage(self):
        image_file, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", "", "Images (*.jpg *.png);; All Files (*)")

        if image_file:
            # input_image = cv.imread(image_file, 0)
            # qimg = QtGui.QImage(input_image.data, input_image.shape[1], input_image.shape[0], QtGui.QImage.Format_RGB888)
            # pixmap = QtGui.QPixmap.fromImage(qimg)
            self.input_img = image_file
            pixmap = QtGui.QPixmap(image_file).scaled(512, 512)
            self.InputScene = QtWidgets.QGraphicsScene()
            self.InputScene.clear()
            self.InputScene.addPixmap(pixmap)
            self.InputImgView.setScene(self.InputScene)
            self.InputImgView.show()

            self.OutputScene = QtWidgets.QGraphicsScene()
            self.OutputScene.clear()
            self.OutputImgView.setScene(self.OutputScene)
            self.OutputImgView.show()
            
        else:
            QtWidgets.QMessageBox.information(None, "Error", "Unable to open image.", QtWidgets.QMessageBox.Ok)


    def sketchImage(self):
        if self.input_img:


            # photocopy input image
            output_img = '.temp/photocopy.png'
            subprocess.call('convert ' + self.input_img + ' -blur 1x2 -colorspace gray -bias 108% -define convolve:scale=10\! -morphology convolve DoG:0,0,6 -resize 512x512 ' + output_img, shell=True)


            # sketch simplify photocopy image
            data  = Image.open(output_img).convert('L')
            w, h  = data.size[0], data.size[1]
            pw    = 8-(w%8) if w%8!=0 else 0
            ph    = 8-(h%8) if h%8!=0 else 0
            data  = ((transforms.ToTensor()(data)-immean)/imstd).unsqueeze(0)


            if pw!=0 or ph!=0:
                data = torch.nn.ReplicationPad2d( (0,pw,0,ph) )( data ).data

            use_cuda = 0
            if use_cuda:
                pred = model.cuda().forward( data.cuda() ).float()
            else:
                pred = model.forward( data )

            final_img = '.temp/sketchsp.png'
            save_image( pred[0], final_img)


            pixmap = QtGui.QPixmap(final_img).scaled(512, 512)
            self.OutputScene = QtWidgets.QGraphicsScene()
            self.OutputScene.clear()
            self.OutputScene.addPixmap(pixmap)
            self.OutputImgView.setScene(self.OutputScene)
            self.OutputImgView.show()
        else:
            QtWidgets.QMessageBox.information(None, "Error", "Input Image not found!", QtWidgets.QMessageBox.Ok)


    def saveImage(self):
        image_file, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", "", "Images (*.jpg *.png);; All Files (*)")
        img = cv.imread('.temp/sketchsp.png')
        if image_file and img is not None:
            cv.imwrite(image_file, img)
        else:
            QQtWidgets.MessageBox.information(self, "Error", "Unable to save image.", QMessageBox.Ok)


    def exitApp(self):
        subprocess.call('rm -rf ./.temp', shell=True)
        self.close()


if __name__ == "__main__":
    
    # load sketch simplification model
    use_cuda = torch.cuda.device_count() > 0
    cache  = load_lua('model_gan.t7')
    model  = cache.model
    immean = cache.mean
    imstd  = cache.std
    model.evaluate()

    # open app
    app = QtWidgets.QApplication(sys.argv)
    subprocess.call('mkdir ./.temp', shell=True)
    window = MainWindowUI()
    sys.exit(app.exec_())
    subprocess.call('rm -rf ./.temp', shell=True)
