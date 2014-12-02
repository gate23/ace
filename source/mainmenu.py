"""
mainmenu.py

This mode contains menu buttons that allow the user to switch between
the modes of the application. It also acts as the home screen.
"""

from PyQt4 import QtCore, QtGui
from enum import ModeEnum

"""
MainMenu:
Contains the title text and mode selection buttons.
"""
class MainMenu(QtGui.QWidget):
    def __init__(self, parent):
        super(MainMenu, self).__init__(parent)

        self.win_ref = parent
        self.initUI()
        
    def initUI(self):
        #Initialize layout for the page
        layout = QtGui.QVBoxLayout()
        layout.setAlignment( QtCore.Qt.AlignHCenter)
        layout.setSpacing(20)
        layout.setContentsMargins(100,150,100,75) #left,right,top,btm
        
        #Create title label
        title = QtGui.QLabel("Algae Counting Tool")
        title_font = QtGui.QFont()
        title_font.setPointSize(36)
        title.setFont(title_font)
        title.setAlignment( QtCore.Qt.AlignHCenter)
        
        #Create selection buttons
        trainer_button = MenuButton("Estimation Trainer")
        stats_button = MenuButton("Estimation Statistics")
        generator_button = MenuButton("Slide Generator")
        
        #Set connections for the buttons
        trainer_button.connect(
                trainer_button,
                QtCore.SIGNAL("pressed()"),
                (lambda: self.win_ref.changeMode(ModeEnum.TRAINER))
        )
        
        stats_button.connect(
                stats_button,
                QtCore.SIGNAL("pressed()"),
                (lambda: self.win_ref.changeMode(ModeEnum.STATS))
        )
        
        generator_button.connect(
                generator_button,
                QtCore.SIGNAL("pressed()"),
                (lambda: self.win_ref.changeMode(ModeEnum.GENERATOR))
        )
        
        #Add title and buttons to the page layout
        layout.addWidget(title)
        layout.addWidget(trainer_button)
        layout.addWidget(stats_button)
        layout.addWidget(generator_button)
        
        self.setLayout(layout)

"""
MenuButton:
Simple class that extends QPushButton so that
menu buttons can be created easily.
"""        
class MenuButton(QtGui.QPushButton):
    font = QtGui.QFont()
    font.setPointSize(28)
    
    def __init__(self, name):
        super(MenuButton, self).__init__()
        
        self.setText(name)
        self.setFont(MenuButton.font)