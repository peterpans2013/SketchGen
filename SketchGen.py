import sys
import subprocess
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 480)
        self.setWindowTitle('Sketch')


        menuBar = self.menuBar()
        file_menu = menuBar.addMenu('File')
        help_menu = menuBar.addMenu('Help')

        open_action = file_menu.addAction('Open')
        save_action = file_menu.addAction('Save')
        quit_action = file_menu.addAction('Quit', self.close)

        open_action.triggered.connect(self.openFile)
        self.show()
    
    def openFile(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            "Select an Image to open...",
            qtc.QDir.homePath(),
            'JPEG Image (*.jpg) ;; PNG Image(*.png) ;; All Files(*)',
            'Image (*.jpg)',
            qtw.QFileDialog.DontUseNativeDialog |
            qtw.QFileDialog.DontResolveSymlinks
        )
        if filename:
            try:
                showImg(self, filename)
            except Exception as e:
                qtw.QMessageBox.critical(self, f"Could not load file: {e}")

    def showImg(self, fileName):
        label = QLabel(self)
        pixmap = qtg.QPixmap(fileName)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
