"""
stats.py

Will eventually display training statistics
**Placeholder right now
"""

from PyQt4 import QtGui, QtCore

class Statistics(QtGui.QWidget):
    def __init__(self, parent,trainer):
        super (Statistics, self).__init__(parent)
        
        self.trainer_ref = trainer
        layout = QtGui.QHBoxLayout()
        
        #placeholder - just displaying # of estimates and total sum right now
        label_estimate = QtGui.QLabel("Total estimates: " + str(self.trainer_ref.estimate_count))
        label_sum = QtGui.QLabel("Total error sum: " + str(self.trainer_ref.error_sum))
        label_session_estimate = QtGui.QLabel("Previous session avg error: " + str(self.trainer_ref.session_error))
        
        layout.addWidget(label_estimate)
        layout.addWidget(label_sum)
        layout.addWidget(label_session_estimate)
        
        self.setLayout(layout)