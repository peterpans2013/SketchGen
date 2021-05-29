# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SketchGen(object):
    def setupUi(self, SketchGen):
        SketchGen.setObjectName("SketchGen")
        SketchGen.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(SketchGen)
        self.centralwidget.setObjectName("centralwidget")
        self.InputImgView = QtWidgets.QGraphicsView(self.centralwidget)
        self.InputImgView.setGeometry(QtCore.QRect(100, 130, 514, 514))
        self.InputImgView.setObjectName("InputImgView")
        self.OutputImgView = QtWidgets.QGraphicsView(self.centralwidget)
        self.OutputImgView.setGeometry(QtCore.QRect(666, 130, 514, 514))
        self.OutputImgView.setObjectName("OutputImgView")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(20, 30, 94, 36))
        self.openButton.setObjectName("openButton")
        self.sketchButton = QtWidgets.QPushButton(self.centralwidget)
        self.sketchButton.setGeometry(QtCore.QRect(130, 30, 94, 36))
        self.sketchButton.setObjectName("sketchButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(240, 30, 94, 36))
        self.saveButton.setObjectName("saveButton")
        SketchGen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SketchGen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 32))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        SketchGen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SketchGen)
        self.statusbar.setObjectName("statusbar")
        SketchGen.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(SketchGen)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(SketchGen)
        self.actionSave.setObjectName("actionSave")
        self.actionSketch = QtWidgets.QAction(SketchGen)
        self.actionSketch.setObjectName("actionSketch")
        self.actionQuit = QtWidgets.QAction(SketchGen)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(SketchGen)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSketch)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(SketchGen)
        QtCore.QMetaObject.connectSlotsByName(SketchGen)

    def retranslateUi(self, SketchGen):
        _translate = QtCore.QCoreApplication.translate
        SketchGen.setWindowTitle(_translate("SketchGen", "SketchGen"))
        self.openButton.setText(_translate("SketchGen", "Open"))
        self.sketchButton.setText(_translate("SketchGen", "Sketch"))
        self.saveButton.setText(_translate("SketchGen", "Save"))
        self.menuFile.setTitle(_translate("SketchGen", "File"))
        self.menuHelp.setTitle(_translate("SketchGen", "Help"))
        self.actionOpen.setText(_translate("SketchGen", "Open"))
        self.actionOpen.setToolTip(_translate("SketchGen", "Open Image"))
        self.actionOpen.setShortcut(_translate("SketchGen", "Ctrl+O"))
        self.actionSave.setText(_translate("SketchGen", "Save"))
        self.actionSave.setToolTip(_translate("SketchGen", "Save Sketch Image"))
        self.actionSave.setShortcut(_translate("SketchGen", "Ctrl+S"))
        self.actionSketch.setText(_translate("SketchGen", "Sketch"))
        self.actionSketch.setToolTip(_translate("SketchGen", "Sketch Input Image"))
        self.actionQuit.setText(_translate("SketchGen", "Quit"))
        self.actionQuit.setToolTip(_translate("SketchGen", "Exit Application"))
        self.actionQuit.setShortcut(_translate("SketchGen", "Ctrl+Q"))
        self.actionAbout.setText(_translate("SketchGen", "About"))
        self.actionAbout.setToolTip(_translate("SketchGen", "About Application"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SketchGen = QtWidgets.QMainWindow()
    ui = Ui_SketchGen()
    ui.setupUi(SketchGen)
    SketchGen.show()
    sys.exit(app.exec_())
