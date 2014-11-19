"""
stats.py

Display training statistics
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  

import pickle
import time
import os.path

from enum import FileEnum,SessionCol
from session import Session
from math import log, fabs


class HistogramView(QListView):
    def __init__(self, parent, splitter):
        super(HistogramView, self).__init__()
        self.parent = parent

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
        painter.drawText(530,250,"Log Error")

        #label each block
        posL = x0 + 25
        for i in xrange(-7,8):
            painter.drawText(posL,y0+20,str(i))
            posL += 20

        #fill in data
        pos = x0 + 20
        max_val = 200

        width = 20
        
        max_in_list = max(self.parent.log_err_list)
        painter.setBrush(Qt.red)
        if (max_in_list != 0):
            for i in range(15):
                if i == 6:
                    painter.setBrush(Qt.blue)
                if i == 9:
                    painter.setBrush(Qt.red)
                height = int((float(self.parent.log_err_list[i]) / max_in_list) * max_val)
                painter.drawRect(QRect(pos,y0 - height,width,height))
                pos += 20 

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
            self.log_err_list = opened[FileEnum.LOG_ERR_LIST]
            self.total_estimates = opened[FileEnum.TOTAL_ESTIMATES]
            
        except:
            self.session_count = 0
            self.error_sum = 0.0
            self.session_list = list()
            self.log_err_list = list()
            for i in range(15):
                self.log_err_list.append(0)
            self.total_estimates = 0
            
    def writeStatsToFile(self):
        stat_list = (self.session_count, self.error_sum, self.session_list, self.log_err_list, self.total_estimates)
        
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

        #move this around
        self.label_estimate = QtGui.QLabel()
        self.label_sum = QtGui.QLabel()

        self.splitter = QSplitter(Qt.Horizontal)

        self.session_table = QtGui.QTableWidget()
        self.session_table.setRowCount(10)
        self.session_table.setColumnCount(6)
        self.session_table.setIconSize(QSize(100, 100))
        self.session_table.verticalHeader().resizeMode(QtGui.QHeaderView.Fixed)
        self.session_table.verticalHeader().setDefaultSectionSize(100)        
        header_labels = QtCore.QStringList()
        header_labels.append("Status")
        header_labels.append("Estimate")
        header_labels.append("Actual")
        header_labels.append("Exact")
        header_labels.append("Log Error")
        header_labels.append("Image")
        self.session_table.setHorizontalHeaderLabels(header_labels)
        session_layout.addWidget(self.session_table)

        self.label_session_score = QtGui.QLabel()
        session_layout.addWidget(self.label_session_score)

        self.updateStatsUI()
        
        return session_layout

    def initLifetimeTab(self):
        lifetime_layout = QtGui.QVBoxLayout()
        
        lifetime_layout.addWidget(self.label_estimate)
        lifetime_layout.addWidget(self.label_sum)

        self.histogram = HistogramView(self,self.splitter)
        lifetime_layout.addWidget(self.histogram)

        self.updateStatsUI()

        return lifetime_layout

    def recordSession(self, session):
        self.session_count += 1
       
        self.error_sum += session.error_sum
        completed_time = time.time() 
        session.time = completed_time
        self.total_estimates += session.total_estimates
        for i in range(15):
            self.log_err_list[i] += session.log_err_list[i]
        
        self.session_list.append(session)
        self.session_box.addItem("Session "+ str(self.session_count))
        self.histogram.dataChanged()

        
    def updateStatsUI(self):
        if self.session_count>0:
            avg_error = self.error_sum/(self.session_count*10)
        else:
            avg_error = 0.0
        
        self.label_estimate.setText("Total estimates: " +
                                    (str(self.session_count*10)))
        err_str = str(avg_error)
        self.label_sum.setText("Lifetime Average Absolute Log Error: " +
                                (err_str))
            
    def updateSessionTable(self, sess_idx):
        if len(self.session_list)+1 >= sess_idx:
            session = self.session_list[sess_idx-1]
            self.session_table.setRowCount(session.length)
            correct_num = 0
            session_log_err = 0
            session_abs_log_err = 0
            
            est_idx = 0
            for estimate in session.estimate_list:
                self.session_table.rowHeight(100)
                log_estimate = log(estimate.estimate, 2)
                log_actual = log(estimate.actual,2)   
                log_error = int(log_estimate) - int(log_actual)
                session_log_err += log_error
                session_abs_log_err += fabs(log_error)
                if log_error == 0:
                    status = "Correct!"
                    correct_num += 1
                else:
                    status = "Incorrect"

                status_item = QtGui.QTableWidgetItem(status)
                self.session_table.setItem(est_idx,SessionCol.STATUS,status_item)     
                
                low = 2**int(log(estimate.estimate,2))
                estimate_str = str(low) + ' - ' + str(low * 2 - 1)
                est_item = QtGui.QTableWidgetItem(estimate_str)
                self.session_table.setItem(est_idx,SessionCol.ESTIMATE,est_item)
                
                low = 2**int(log(estimate.actual,2))
                actual_str = str(low) + ' - ' + str(low * 2 - 1)
                actual_item = QtGui.QTableWidgetItem(str(actual_str))
                self.session_table.setItem(est_idx,SessionCol.ACTUAL,actual_item)
                
                exact_item = QtGui.QTableWidgetItem(str(int(estimate.actual)))
                self.session_table.setItem(est_idx,SessionCol.EXACT,exact_item)
                
                diff_item = QtGui.QTableWidgetItem(str(log_error))
                self.session_table.setItem(est_idx,SessionCol.LOG_ERROR,diff_item)
                
                #image
                icon = QtGui.QIcon()
                
                imagePath = session.image_list[est_idx]
                if (imagePath):
                    icon.addPixmap(QtGui.QPixmap(os.path.join(os.path.curdir, imagePath)))
                    image_item = QtGui.QTableWidgetItem(icon, "")
                    image_item.setSizeHint(QSize(100, 100))
                    self.session_table.setItem(est_idx,SessionCol.IMAGE,image_item)
                
                est_idx +=1

            self.label_session_score.setText('Score: ' + str(correct_num) + '/' + str(session.length) +
                                              '\tSession Average Log Error: ' + 
                                              str(session_log_err/session.length) +
                                              '\tSession Average Absolute Log Error: ' + 
                                              str(session_abs_log_err/session.length))


        else:
            #TODO: this should never happen, but if it does actually raise an err
            print "session nonexistent"