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
    
    """
    initPages():
        Creates and populates a QStackedWidget that contains the different
        modes (i.e. pages) of the application.
    """
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
    
    """
    initMenuBar():
        Creates a menu bar that is visible from any mode of the application.
        The options under the menus are called "actions".
    """
    def initMenuBar(self):
        menu_bar = self.menuBar()
        
        #Create File menu and actions.
        file_menu = menu_bar.addMenu('&File')
        
        to_menu_action = QtGui.QAction('Main Menu', self)
        to_menu_action.triggered.connect(lambda: self.changeMode(ModeEnum.MENU))
        
        exit_action = QtGui.QAction('Exit', self)
        exit_action.triggered.connect(self.exitProgram )
        
        file_menu.addAction(to_menu_action)
        file_menu.addAction(exit_action)
        
        #Create Help menu and actions.
        help_menu = menu_bar.addMenu('&Help')

        about_action = QtGui.QAction('About', self)
        about_action.triggered.connect(self.aboutMenu)
        help_menu.addAction(about_action)
        
    """
    changeMode(page_num):
        Changes the view of the user to the mode associated with page_num.
        page_num is an integer defined by ModeEnum. (see enum module).
        
        Special conditions that need to be met before switching to a mode
        may be addressed here.
    """
    def changeMode(self, page_num):
        #Perform any work that needs to be done before switching modes.
        if page_num == ModeEnum.STATS:
            #Update the stats page before switching the view.
            self.stats.updateStatsUI()

        elif page_num == ModeEnum.TRAINER:
            #Attempt to start a new Trainer session if there is not
            #an active session.
            if (not self.trainer.has_active_session):
                if (not self.trainer.startNewSession()):
                    return

        #Switch the mode.
        self.mode_stack.setCurrentIndex(page_num)

    """
    exitProgram():
    This exit routine is called when the user exits via File->Exit.
    Writes the stats to disk and closes the application.
    """
    def exitProgram(self):
        self.mode_stack.widget(ModeEnum.STATS).writeStatsToFile()
        QtGui.qApp.quit()
    
        
    """
    closeEvent(event):
    This exit routine is an overloaded version of Qt's closeEvent,
    and normally occurs when the user exits by clicking the 'X'.
    Before accepting the close event, stats are written to disk.
    """
    def closeEvent(self, event):
        self.mode_stack.widget(ModeEnum.STATS).writeStatsToFile()
        event.accept()
        
        
    def aboutMenu(self):
        QtGui.QMessageBox.about(self, 'About',
            '''<p>For those who require assistance in the counting of blue-green algae,
                the Algae Count Estimator (ACE) is a tool that graphically generates algae 
                colonies with known counts. Users may test their ability to count these
                colonies with this program and be provided statistics regarding how they've done.</p>
                <p>For more info, see the User's Manual located in the Docs folder.</p>
                <p>This program was originally commissioned for the Institute for Watershed Studies
                of Western Washington University.</p>
                <p>Authors: Samuel Dunlap, Josh Minor, Matt Ralphs, Andrew Young</p>''')
        
