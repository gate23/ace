"""
mainwindow.py

Holds the MainWindow class, top level widget of the application.
MainWindow has instances of each page in a stacked widget, and 
is responsible for switching between them.
"""

from PyQt4 import QtCore, QtGui
from mainmenu import MainMenu
from trainer import Trainer
from stats import Statistics
from generator import Generator
from enum import ModeEnum

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()        
        
        self.setWindowTitle("Algae Count Estimator")
        
        self.setSizePolicy(QtGui.QSizePolicy.Fixed,
                           QtGui.QSizePolicy.Fixed)
        
        self.setFixedSize(QtCore.QSize(800,620))
        
        self.initPages()
        self.initMenuBar()       
        
        self.show()
    
    #creates QStackedWidget to contain the different modes (pages)
    #populates the stacked widget with instances of the modes
    def initPages(self):
        self.mode_stack = QtGui.QStackedWidget()

        main_menu = MainMenu(self) #0
        self.stats = Statistics(self) #1
        self.trainer = Trainer(self,self.stats) #2
        self.generator = Generator(self) #3
        
        self.mode_stack.addWidget(main_menu)
        self.mode_stack.addWidget(self.stats)
        self.mode_stack.addWidget(self.trainer)
        self.mode_stack.addWidget(self.generator)
        
        self.setCentralWidget(self.mode_stack)
                
    def initMenuBar(self):
        menu_bar = self.menuBar()
        
        file_menu = menu_bar.addMenu('&File')
        to_menu_action = QtGui.QAction('Main Menu', self)
        to_menu_action.triggered.connect(lambda: self.changeMode(ModeEnum.MENU))
        
        exit_action = QtGui.QAction('Exit', self)
        exit_action.triggered.connect(self.exitProgram )
        
        file_menu.addAction(to_menu_action)
        file_menu.addAction(exit_action)
        
        
        help_menu = menu_bar.addMenu('&Help')
        
        about_action = QtGui.QAction('About', self)
        
        help_menu.addAction(about_action)
        
        
    def changeMode(self, page_num):
        if   page_num == ModeEnum.GENERATOR:
            pass
        
        elif page_num == ModeEnum.STATS:
            self.stats.updateStatsUI()

        elif page_num == ModeEnum.TRAINER:
            if (not self.trainer.has_active_session):
                if (not self.trainer.startNewSession()):
                    return

        self.mode_stack.setCurrentIndex(page_num)
        
    #for closing via File->Exit
    def exitProgram(self):
        self.mode_stack.widget(ModeEnum.STATS).writeStatsToFile()
        QtGui.qApp.quit()
    
        
    #for closing via 'X' window button
    def closeEvent(self, event):
        self.mode_stack.widget(ModeEnum.STATS).writeStatsToFile()
        event.accept()
