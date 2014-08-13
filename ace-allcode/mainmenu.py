"""
mainmenu.py

MainMenu: switch between modes!
"""

from PyQt4 import QtCore, QtGui
from enum import ModeEnum

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
        trainer_button = TitleButton("Estimation Trainer")
        editor_button = TitleButton("Slide Editor")
        stats_button = TitleButton("Estimation Statistics")
        
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
        
        editor_button.connect(
                editor_button,
                QtCore.SIGNAL("pressed()"),
                (lambda: self.win_ref.changeMode(ModeEnum.EDITOR))
        )
        
        #Add title and buttons to the page layout
        layout.addWidget(title)
        layout.addWidget(trainer_button)
        layout.addWidget(stats_button)
        layout.addWidget(editor_button)
        
        self.setLayout(layout)

class TitleButton(QtGui.QPushButton):
    font = QtGui.QFont()
    font.setPointSize(28)
    

    def __init__(self, name):
        super(TitleButton, self).__init__()
        
        self.setText(name)
        self.setFont(TitleButton.font)