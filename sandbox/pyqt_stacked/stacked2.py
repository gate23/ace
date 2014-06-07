#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a simple
window in PyQt4.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#extends a QtGui.QWidget
class Example(QtGui.QMainWindow):
    

    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()

        #add stacked widgit
        self.stackedWidget = QtGui.QStackedWidget()

        #add layout
        mainWidget = QWidget()
        mainLayout = QVBoxLayout()
        #add stuff to layout

        #make a button
        btn = QtGui.QPushButton('Quit', self)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')

        #quit with button click
        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.clicked.connect(self.close)
        btn.resize(btn.sizeHint())
        btn.show()
        mainLayout.addWidget(btn)


        mainWidget.setLayout(mainLayout)
        self.stackedWidget.addWidget(mainWidget)
       
    def initUI(self):
        #tooltip help
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        # self.setGeometry(300, 300, 250, 150)
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('My Test App')
        #does not show up in gnome
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        #create the action
        exitAction = QtGui.QAction(QtGui.QIcon('icon.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        #create the action
        testAction = QtGui.QAction(QtGui.QIcon('icon.png'), 'Test', self)
        testAction.setShortcut('Ctrl+T')
        testAction.setStatusTip('Test Action')
        # exitAction.triggered.connect(self.close)

        aboutAction = QtGui.QAction(QtGui.QIcon('icon.png'), 'About', self)
        aboutAction.setShortcut('Ctrl+A')
        aboutAction.setStatusTip('Test Action')
        #do something


        #create the menu bar
        sbar = self.statusBar()
        mbar = self.menuBar()
        tbar = self.addToolBar('Exit')

        fileMenu = mbar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        editMenu = mbar.addMenu('&Edit')
        editMenu.addAction(testAction)

        viewMenu = mbar.addMenu('&View')
        viewMenu.addAction(testAction)

        toolsMenu = mbar.addMenu('&Tools')
        toolsMenu.addAction(testAction)

        #setup the about menu
        helpMenu = mbar.addMenu('&Help')
        helpMenu.addAction(aboutAction)

        #this is the toolbar
        tbar.addAction(exitAction)




    
        self.show()

    def center(self):
        fg = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

        #watcher for the close event (in the file menu)
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure you want to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def quitEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure you want to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



def main():
    
    #the main application object
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
