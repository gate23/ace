"""
trainer.py

Trainer is the class representing the trainer mode (duh)
Makes use of SlideGen class for generating and viewing slides
"""

from PyQt4 import QtGui, QtCore
from slide_gen import SlideGen
from slide_scene import SlideScene
from enum import ModeEnum
from session import Session,Estimate
from math import log, fabs
import time
import os.path

class Trainer(QtGui.QWidget):
    SLIDE_WIDTH,SLIDE_HEIGHT = 540,540
    LOW_POW2, HIGH_POW2 = 3,10 #defines upper and lower ranges 
    
    def __init__(self, parent, stats):
        super(Trainer,self).__init__(parent)
        self.parent = parent
        self.estimate_number = 1
        self.max_session_length = 100
        self.has_active_session = False
        self.stats_ref = stats #stats instance

        max_count = 2**(Trainer.HIGH_POW2+1) -1        
        self.slide_gen = SlideGen(self, 2, max_count)
        
        self.initUI()
        
    def initUI(self):
        slide_layout = self.initSlideLayout()
        estimate_layout = self.initEstimateLayout()
        
        layout = QtGui.QHBoxLayout()        
        layout.addLayout(slide_layout)
        layout.addLayout(estimate_layout)
        self.setLayout(layout)
    
    """
    QVBoxLayout self.initSlideLayout():
        Called by self.initUI() during initialization to build the scene, view,
        and focus controls for the slide.
    """
    def initSlideLayout(self):
        self.slide_scene = SlideScene(QtCore.QRectF(0,
                                                    0,
                                                    self.SLIDE_WIDTH,
                                                    self.SLIDE_HEIGHT), 
                                                    self) #trainer is parent
                                          
        #build the view
        self.view = QtGui.QGraphicsView(self.slide_scene,
                                        self) #trainer is parent
        #disable scroll bars
        self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        self.view.setSizePolicy(QtGui.QSizePolicy.Fixed,
                                QtGui.QSizePolicy.Fixed)        
    
        focus_layout = QtGui.QHBoxLayout()

        #build focus controls
        focus_text = QtGui.QLabel("Focus: ")
        self.focus_slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.focus_slider.setTickInterval(25)
        self.focus_slider.setSliderPosition((self.slide_scene.current_focus+1)*15)
        
        focus_plus_btn = QtGui.QPushButton("+")
        focus_minus_btn = QtGui.QPushButton("-")
        focus_plus_btn.setMaximumWidth(25)
        focus_minus_btn.setMaximumWidth(25)

        #connect         
        focus_plus_btn.connect(focus_plus_btn, QtCore.SIGNAL("pressed()"),
                        self.slide_scene.focusUp)
        focus_minus_btn.connect(focus_minus_btn, QtCore.SIGNAL("pressed()"),
                        self.slide_scene.focusDown)
        
        self.focus_slider.valueChanged.connect(self.slide_scene.sliderFocus)

        #add controls
        focus_layout.addWidget(focus_text)
        focus_layout.addWidget(focus_minus_btn)
        focus_layout.addWidget(focus_plus_btn)
        focus_layout.addWidget(self.focus_slider)
        
        layout = QtGui.QVBoxLayout()
        
        layout.addWidget(self.view)
        layout.addLayout(focus_layout)
        
        return layout
    """
    QVBoxLayout self.initEstimateLayout():
        Called by self.initUI() to build the range buttons, submission button,
        and feedback display for estimates.
    """
    def initEstimateLayout(self):
        widget = QtGui.QWidget(self)
        self.guess_group = QtGui.QButtonGroup(widget)

        #create range selector buttons        
        for _range in range(Trainer.LOW_POW2, Trainer.HIGH_POW2+1):
            low = 2**_range
            high = 2*low -1
            btn_str = str(low)+"-"+str(high) 
            temp_btn = QtGui.QRadioButton(btn_str)
            
            #add the button as a member of the class so it persists
            member_name = "r"+str(_range)
            setattr(self, member_name, temp_btn);
            btn = getattr(self, member_name)
            self.guess_group.addButton( btn)
            self.guess_group.setId(btn, _range)
            
        getattr(self,"r"+str(Trainer.LOW_POW2)).setChecked(True)
        #button to submit estimate
        button = QtGui.QPushButton("Estimate Algae Count")
        button.connect( button, QtCore.SIGNAL("pressed()"),
                        self.submitEstimate)

        self.estimate_display = QtGui.QTextEdit()
        self.estimate_display.setReadOnly(True)

        #guess_label: shows which number guess user is making
        self.estimate_label = QtGui.QLabel("Slide " +  str(self.estimate_number) + "/10")      
        
        estimate_layout = QtGui.QVBoxLayout()
        estimate_layout.addWidget(self.estimate_label)
        estimate_layout.addWidget(self.estimate_display)
        buttons = self.guess_group.buttons()
        for btn in buttons:
            estimate_layout.addWidget(btn)
        estimate_layout.addWidget(button)
        
        return estimate_layout
    
    """
    blah blah test test
    """    
    def submitEstimate(self):
        pow2_range = self.guess_group.checkedId() 
        
        if (pow2_range):
            estimate = 2**pow2_range
        else:
            return False
            
        estimate_range = str(estimate) + '-' + str(estimate * 2 - 1)

        actual = self.slide_scene.count()

        log_estimate = int(log(estimate, 2))
        log_actual = int(log(actual,2))

        low = 2**int(log(actual,2))
        actual_range = str(low) + '-' + str(low * 2 - 1)
        
        log_error = log_estimate - log_actual

        if log_error == 0:
            status = " - Correct!"
        else:
            status = " - Incorrect"

        self.estimate_display.append(
                "Slide " + str(self.estimate_number) + status +
                "\nEstimate: " + estimate_range +
                "\nActual Range: " + actual_range +
                "\nExact Count: " + str(actual) +
                "\nLog Error: " + str(log_error) + "\n")

        #add estimate to list
        this_estimate = Estimate(estimate, actual)
        self.current_session.addEstimate(this_estimate)

        
        self.current_session.error_sum += fabs(log_error)
        self.current_session.total_estimates += 1
        bias = 7
        self.current_session.log_err_list[log_error+bias] += 1
        filename = "thum_"+str(int(round(time.time())))+"_"+str(self.estimate_number)+".png"
        imagePath = os.path.normpath("./session/"+filename)
        self.current_session.addImage(self.slide_scene.save_image(imagePath, 100, 100))

        #update display            
        self.estimate_label.setText("Slide " +  str(self.estimate_number) + "/" + str(self.num_slides))
        if (not self.current_session.isComplete() ):
            self.slide_gen.genSlide(self.slide_scene)
            self.estimate_number += 1
                       
        else:
            self.stats_ref.recordSession(self.current_session)
            
            #display stats for 10-estimate session
            session_error = self.current_session.error_sum / self.num_slides
            
            self.estimate_display.append("\nSession complete!")
            self.estimate_display.append("Average log error for this session: " + 
                                            str(session_error) + "\n")

            #MessageBox - restart trainer or return to menu
            self.endMessage = QtGui.QMessageBox.question(self,'Message',
                 "Session complete! Try again?",
                 QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)

            if self.endMessage == QtGui.QMessageBox.Yes:
                self.startNewSession()
            elif self.endMessage == QtGui.QMessageBox.No:
                self.has_active_session = False
                self.parent.changeMode(ModeEnum.MENU)

    #when session is complete, reset stuff
    def startNewSession(self):
        self.estimate_sum = 0
        self.actual_sum = 0
        self.estimate_number = 1
        
        session_length_input = QtGui.QInputDialog(self)     
        
        self.num_slides, ok = QtGui.QInputDialog.getInt(self, 'Trainer', 
            'How many algae slides would you like to generate?',
            10, 1, self.max_session_length)

        if ok:
            self.has_active_session = True
            self.estimate_label.setText("Slide " +  str(self.estimate_number) + "/" +
                str(self.num_slides))
            
            self.estimate_display.append("Beginning new session...")

            #pass slide to slide_gen
            self.slide_gen.genSlide(self.slide_scene)
            self.current_session = Session(self.num_slides)
            self.focus_slider.setSliderPosition((self.slide_scene.current_focus+1)*15)
            return True
        else:
            self.has_active_session = False
            return False

    def mousePressEvent(self, event):
        self.slide_gen.saveSlide(self.slide_scene)
