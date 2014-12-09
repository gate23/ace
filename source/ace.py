"""
ace.py

Entry point of the application.

"""
import sys
from PyQt4 import QtGui, QtCore
from mainwindow import MainWindow
import os

def main():
    
    
    
    #build required directories
    if not os.path.exists(os.path.join(os.curdir, 'session')):
        os.makedirs(os.path.join(os.curdir, 'session'))
        
    if not os.path.exists(os.path.join(os.curdir, 'slide')):
        os.makedirs(os.path.join(os.curdir, 'slide'))
    

    app = QtGui.QApplication(sys.argv) 

    app_icon = QtGui.QIcon()
    app_icon.addFile('img/icons/16x16.png', QtCore.QSize(16,16))
    app_icon.addFile('img/icons/24x24.png', QtCore.QSize(24,24))
    app_icon.addFile('img/icons/32x32.png', QtCore.QSize(32,32))
    app_icon.addFile('img/icons/48x48.png', QtCore.QSize(48,48))
    app_icon.addFile('img/icons/64x64.png', QtCore.QSize(64,64))
    app_icon.addFile('img/icons/96x96.png', QtCore.QSize(96,96))
    app_icon.addFile('img/icons/128x128.png', QtCore.QSize(128,128))
    app_icon.addFile('img/icons/256x256.png', QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)
    
    main_window = MainWindow() 

    sys.exit(app.exec_() )

if __name__ == "__main__":
    main()