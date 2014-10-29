"""
stats.py

Display training statistics
"""

from PyQt4 import QtGui, QtCore

import pickle

class Statistics(QtGui.QWidget):
    def __init__(self, parent):
        super (Statistics, self).__init__(parent)
        self.loadStatsFromFile()
        self.initUI()
        
    
    def loadStatsFromFile(self):
        try:
            file = open('stats.ace')
            opened = pickle.load(file)
            
            self.session_count = opened[0]
            self.error_sum = opened[1]
            
        except:
            self.session_count = 0
            self.error_sum = 0.0
            
    def writeStatsToFile(self):
        stat_list = (self.session_count, self.error_sum)
        
        output = open('stats.ace','wb')
        pickle.dump(stat_list, output)
        
        output.close()

            
    def initUI(self):
        layout = QtGui.QHBoxLayout()

        stats_tabs = QtGui.QTabWidget()
        session_tab = QtGui.QWidget()
        lifetime_tab = QtGui.QWidget()
        stats_tabs.addTab(session_tab,"Session")
        stats_tabs.addTab(lifetime_tab,"Lifetime")
        
        sessionLayout = self.initSessionTab()
        session_tab.setLayout(sessionLayout)
        lifetimeLayout = self.initLifetimeTab()
        lifetime_tab.setLayout(lifetimeLayout)

        layout.addWidget(stats_tabs)
        self.setLayout(layout)

    def initSessionTab(self):
        session_layout = QtGui.QVBoxLayout()

        session_box = QtGui.QComboBox()
        session_box.addItem("Select session...")
        session_box.addItem("Session 1 - Test session")
        session_layout.addWidget(session_box)

        #Currently useless, will add useful stats later
        session_top_layout = QtGui.QHBoxLayout()
        #move this around
        self.label_estimate = QtGui.QLabel()
        self.label_sum = QtGui.QLabel()
        #session_top_layout.addWidget(self.label_estimate)
        #session_top_layout.addWidget(self.label_sum)
        session_layout.addLayout(session_top_layout)


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

        session_layout.addWidget(test_table)

        self.updateStatsUI()
        
        return session_layout

    def initLifetimeTab(self):
        lifetime_layout = QtGui.QVBoxLayout()
        
        lifetime_layout.addWidget(self.label_estimate)
        lifetime_layout.addWidget(self.label_sum)
        test_label = QtGui.QLabel("YO PUT A GRAPH HERE.")
        lifetime_layout.addWidget(test_label)

        self.updateStatsUI()

        return lifetime_layout

    def recordSession(self, error):
        self.session_count += 1
        self.error_sum += error

    def updateStatsUI(self):
        if self.session_count>0:
            error = self.error_sum/self.session_count
        else:
            error = 0.0
        
        self.label_estimate.setText("Total estimates: " +
                                    (str(self.session_count*10)))
        self.label_sum.setText("Lifetime Average Error: " +
                                (str(error)))
        


    