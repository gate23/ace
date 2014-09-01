"""
trainer.py

Trainer is the class representing the trainer mode (duh)
Makes use of SlideGen class for generating and viewing slides
"""

import math
import pickle

from PyQt4 import QtGui, QtCore
from slidegen import SlideGen

MAX_ESTIMATE = 9999

class Trainer(QtGui.QWidget):
    def __init__(self, parent):
        super(Trainer,self).__init__(parent)
        
        self.initUI()
        
    def initUI(self):
        layout = QtGui.QHBoxLayout()
        
        self.slide_display = SlideGen(self)
        self.slide_display.genSlide()
        
        #estimate_entry: input line for estimate
        self.estimate_entry = QtGui.QLineEdit()
        validator = QtGui.QIntValidator(0,MAX_ESTIMATE,self.estimate_entry)
        self.estimate_entry.setValidator(validator)
        
        #button to submit estimate
        button = QtGui.QPushButton("Estimate Algae Count")
        button.connect( button, QtCore.SIGNAL("pressed()"),
                        self.submitEstimate)
        #allow Enter press to submit estimate
        self.estimate_entry.connect(
                self.estimate_entry, QtCore.SIGNAL("returnPressed()"),
                button, QtCore.SIGNAL("pressed()")  )
        
        #estimate_display: shows list of previous estimates
        self.estimate_display = QtGui.QTextEdit()
        self.estimate_display.setReadOnly(1)
        
        
        estimate_layout = QtGui.QVBoxLayout()
        estimate_layout.addWidget(self.estimate_display)
        estimate_layout.addWidget(button)
        estimate_layout.addWidget(self.estimate_entry)
        
        
        layout.addWidget(self.slide_display)
        layout.addLayout(estimate_layout)
        
        self.setLayout(layout)
        
        #stats stuff
        try:
            file = open('stats.ace')
            opened = pickle.load(file)
            
            self.estimate_count = opened[0]
            self.error_sum = opened[1]
            
            print opened
            
        except:
            self.estimate_count = 0
            self.error_sum = 0.0
        
    def submitEstimate(self):
        if self.estimate_entry.text().length() > 0 :            
            estimate = float(self.estimate_entry.text())
            actual = float(self.slide_display.count())
                 
            raw_percent_err = (math.fabs(estimate - actual) / actual) * 100.0

            self.estimate_count += 1   
            self.error_sum += raw_percent_err
            print "Total Average Err: " + str(self.error_sum/self.estimate_count)           
            
            #format for less precision
            percent_err = "{:.2f}".format(raw_percent_err)
            

        if self.estimate_entry.text().length() > 0 :
            self.estimate_display.append(
                    "Estimate: " + str(self.estimate_entry.text()) +
                    " Actual Count: " + str(self.slide_display.count()) )
            self.estimate_entry.clear()
            
            self.slide_display.genSlide()
            
    def dumpStats(self):
        print "dumping stats"
        
        stat_list = (self.estimate_count, self.error_sum)
        
        output = open('stats.ace','wb')
        pickle.dump(stat_list, output)
        
        output.close()
             
        