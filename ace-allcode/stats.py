"""
stats.py

Display training statistics
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  

import pickle
import time
import math
import os.path

from enum import FileEnum,SessionCol
from session import Session


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

        pos = x0 + 20

        width = 20
        painter.setBrush(Qt.red)
        painter.drawRect(QRect(pos,y0 - 1 * 10,width,1 * 10)) 
        painter.drawRect(QRect(pos+20,y0 - 2 * 10,width,2 * 10)) 
        painter.setBrush(Qt.blue)
        painter.drawRect(QRect(pos+40,y0 - 3 * 10,width,3 * 10)) 
        painter.drawRect(QRect(pos+60,y0 - 4 * 10,width,4 * 10)) 
        painter.drawRect(QRect(pos+80,y0 - 5 * 10,width,5 * 10)) 
        painter.setBrush(Qt.red)
        painter.drawRect(QRect(pos+100,y0 - 6 * 10,width,6 * 10)) 
        painter.drawRect(QRect(pos+120,y0 - 7 * 10,width,7 * 10)) 

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
            
            self.session_count = opened[FileEnum.SESSION_COUNT]
            self.error_sum = opened[FileEnum.ERROR_SUM]
            self.session_list = opened[FileEnum.SESSION_LIST]
            
        except:
            self.session_count = 0
            self.error_sum = 0.0
            self.session_list = list()
            
    def writeStatsToFile(self):
        stat_list = (self.session_count, self.error_sum, self.session_list)
        
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
        
        session_layout = self.initSessionTab()
        session_tab.setLayout(session_layout)
        lifetime_layout = self.initLifetimeTab()
        lifetime_tab.setLayout(lifetime_layout)

        layout.addWidget(stats_tabs)
        self.setLayout(layout)

    def initSessionTab(self):
        session_layout = QtGui.QVBoxLayout()

        self.session_box = QtGui.QComboBox()
        self.session_box.addItem("Select session...")
        session_layout.addWidget(self.session_box)
        
        for i in range(1,self.session_count+1):
            self.session_box.addItem("Session "+str(i))
        
        self.connect( self.session_box, QtCore.SIGNAL("currentIndexChanged(int)"),
                        self.updateSessionTable)

        #Currently useless, will add useful stats later
        session_top_layout = QtGui.QHBoxLayout()
        #move this around
        self.label_estimate = QtGui.QLabel()
        self.label_sum = QtGui.QLabel()
        self.splitter = QSplitter(Qt.Horizontal)
        

        #session_top_layout.addWidget(self.label_estimate)
        #session_top_layout.addWidget(self.label_sum)
        session_layout.addLayout(session_top_layout)

        self.session_table = QtGui.QTableWidget()
        self.session_table.setRowCount(10)
        self.session_table.setColumnCount(5)
        self.session_table.setIconSize(QSize(100, 100))
        
        self.session_table.verticalHeader().resizeMode(QtGui.QHeaderView.Fixed)
        self.session_table.verticalHeader().setDefaultSectionSize(100)        

        header_labels = QtCore.QStringList()
        header_labels.append("Estimate")
        header_labels.append("Actual")
        header_labels.append("Difference")
        header_labels.append("Error")
        header_labels.append("Image")
        self.session_table.setHorizontalHeaderLabels(header_labels)
        
        session_layout.addWidget(self.session_table)

        histogram = HistogramView(self.splitter)
        session_layout.addWidget(histogram)

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

    def recordSession(self, session):
        self.session_count += 1
       
        self.error_sum += session.error_sum
        completed_time = time.time() 
        session.time = completed_time
        
        self.session_list.append(session)
        self.session_box.addItem("Session "+str(self.session_count))
        
    def updateStatsUI(self):
        if self.session_count>0:
            error = self.error_sum/(self.session_count*10)
        else:
            error = 0.0
        
        self.label_estimate.setText("Total estimates: " +
                                    (str(self.session_count*10)))
        err_str = str("{:.1f}".format(error))
        self.label_sum.setText("Lifetime Average Error: " +
                                (err_str) +"%")
            
    def updateSessionTable(self, sess_idx):
        if len(self.session_list)+1 >= sess_idx:
            session = self.session_list[sess_idx-1]
            est_idx = 0
            for estimate in session.estimate_list:
                self.session_table.rowHeight(100);        
                
                est_item = QtGui.QTableWidgetItem(str(int(estimate.estimate)))
                self.session_table.setItem(est_idx,SessionCol.ESTIMATE,est_item)
                
                actual_item = QtGui.QTableWidgetItem(str(int(estimate.actual)))
                self.session_table.setItem(est_idx,SessionCol.ACTUAL,actual_item)
                
                diff_item = QtGui.QTableWidgetItem()
                diff = math.fabs(estimate.estimate - estimate.actual)
                diff_str = str(int(diff))
                diff_item.setText(diff_str)
                self.session_table.setItem(est_idx,SessionCol.DIFF,diff_item)
                
                err_item = QtGui.QTableWidgetItem()
                err = "{:.2f}".format((diff/estimate.actual)*100)
                err_str = str(err)+"%"
                err_item.setText(err_str)
                self.session_table.setItem(est_idx,SessionCol.ERROR,err_item)
                
                #image
                icon = QtGui.QIcon()
                
                imagePath = session.image_list[est_idx]
                if (imagePath):
                    icon.addPixmap(QtGui.QPixmap(os.path.join(os.path.curdir, imagePath)))
                    image_item = QtGui.QTableWidgetItem(icon, "")
                    image_item.setSizeHint(QSize(100, 100))
                    self.session_table.setItem(est_idx,SessionCol.IMAGE,image_item)
                
                est_idx +=1
        else:
            #TODO: this should never happen, but if it does actually raise an err
            print "session nonexistent"



    
