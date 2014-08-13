"""
stats.py

Will eventually display training statistics
**Placeholder right now
"""

from PyQt4 import QtGui, QtCore

class Statistics(QtGui.QWidget):
    def __init__(self, parent):
        super (Statistics, self).__init__(parent)
        
        layout = QtGui.QHBoxLayout()
        
        label = QtGui.QLabel("Statistics")
        
        layout.addWidget(label)
        
        self.setLayout(layout)