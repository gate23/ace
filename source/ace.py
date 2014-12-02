"""
ace.py

Entry point of the application.

"""
import sys
from PyQt4 import QtGui
from mainwindow import MainWindow

def main():

    app = QtGui.QApplication(sys.argv) 
    
    main_window = MainWindow() 

    sys.exit(app.exec_() )

if __name__ == "__main__":
    main()