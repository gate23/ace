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
        self.currentStats = {}
        self.updateStats()
        self.initUI()

    def initUI(self):
        layout = QtGui.QHBoxLayout()
        statLayout = self.initStatLayout()
        layout.addLayout(statLayout)

        self.setLayout(layout)

    def initStatLayout(self):
        layout = QtGui.QVBoxLayout()

        top_layout = QtGui.QHBoxLayout()
        
        self.label_estimate = QtGui.QLabel("Total estimates: " +
            str(self.currentStats['totalEstimates']))
        self.label_sum = QtGui.QLabel("Total error sum: " +
            str(self.currentStats['totalError']))
        self.label_session_estimate = QtGui.QLabel("Previous session avg error: "  +
            str(self.currentStats['prevAvgError']))
        top_layout.addWidget(self.label_estimate)
        top_layout.addWidget(self.label_sum)
        top_layout.addWidget(self.label_session_estimate)
        layout.addLayout(top_layout)

        test_table = QtGui.QTableWidget()
        test_table.setRowCount(10)
        test_table.setColumnCount(5)

        header_labels = QtCore.QStringList()
        header_labels.append("Guessed")
        header_labels.append("Actual")
        header_labels.append("Difference")
        header_labels.append("Error")
        header_labels.append("Image")
        test_table.setHorizontalHeaderLabels(header_labels)

        test_item = QtGui.QTableWidgetItem("test")
        test_table.setItem(0,0,test_item)

        layout.addWidget(test_table)

        return layout

    #TODO: Check trainer, this isn't updating estimates/error properly
    def updateStats(self):
        self.currentStats['totalEstimates'] = self.trainer_ref.estimate_count
        self.currentStats['totalError'] = self.trainer_ref.error_sum
        self.currentStats['prevAvgError'] = self.trainer_ref.session_error

    def updateStatsUI(self):
        self.label_estimate = QtGui.QLabel("Total estimates: " +
            str(self.currentStats['totalEstimates']))
        self.label_sum = QtGui.QLabel("Total error sum: " +
            str(self.currentStats['totalError']))
        self.label_session_estimate.setText("Previous session avg error: " +
            str(self.currentStats['prevAvgError']))