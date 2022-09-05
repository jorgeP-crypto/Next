from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys
from os import environ
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
# import main as m
# import main
# from main_program import *

# class MainThread(QThread):
    
#     def __init__(self):
#         super(MainThread, self).__init__()
        

#     def run(self):
#         Main.Process_audio()

        

# startExe = MainThread()

# Process_audio()

class Ui_Next(object):

    def setupUi(self, Next):
        Next.setObjectName("Next")
        Next.resize(730, 485)
        self.centralwidget = QtWidgets.QWidget(Next)
        self.centralwidget.setObjectName("centralwidget")
        self.bg1 = QtWidgets.QLabel(self.centralwidget)
        self.bg1.setGeometry(QtCore.QRect(-190, -170, 1171, 811))
        # self.bg1.setText("")
        self.bg1.setPixmap(QtGui.QPixmap("C:/Users/Fibre/projectNext/Next/Black_Template.jpg"))
        self.bg1.setObjectName("bg1")

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -60, 601, 451))
        self.label.setMinimumSize(QtCore.QSize(600, 600))
        self.label.setMaximumSize(QtCore.QSize(600, 600))
        self.label.setObjectName("label")
        
        Next.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Next)
        self.statusbar.setObjectName("statusbar")
        Next.setStatusBar(self.statusbar)

        # add label to main window
        Next.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QMovie("C:/Users/Fibre/projectNext/Next/Aqua.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        
        
    # startExe.start()


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

suppress_qt_warnings()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_Next()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

# m.Process_audio()

