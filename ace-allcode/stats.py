"""
stats.py

Display training statistics
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  

import pickle

class HistogramView(QListView):
    def __init__(self, parent):
        super(HistogramView, self).__init__()

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self.viewport())
        painter.setPen(Qt.black)

        x0 = 40
        y0 = 250

    #y-axis
        painter.drawLine(x0,y0,40,30)
    #arrow at end of axis  
        painter.drawLine(38,32,40,30)  
        painter.drawLine(40,30,42,32)  
          
    #x-axis
        painter.drawLine(x0,y0,520,250)
    #arrow at end of x-axis  
        painter.drawLine(518,248,520,250)  
        painter.drawLine(520,250,518,252)
    #x-axis label  
        painter.drawText(530,250,"Log Difference")

    def dataChanged(self):
        self.viewport().update()


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
        statLayout = self.initStatLayout()
        layout.addLayout(statLayout)

        self.setLayout(layout)

    def initStatLayout(self):
        layout = QtGui.QVBoxLayout()

        top_layout = QtGui.QHBoxLayout()
        
        self.label_estimate = QtGui.QLabel()
        self.label_sum = QtGui.QLabel()
        self.splitter = QSplitter(Qt.Horizontal)
        
        
        top_layout.addWidget(self.label_estimate)
        top_layout.addWidget(self.label_sum)
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

        histogram = HistogramView(self.splitter)
        layout.addWidget(histogram)

        self.updateStatsUI()
        
        return layout

    #TODO: Check trainer, this isn't updating estimates/error properly
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


        



    