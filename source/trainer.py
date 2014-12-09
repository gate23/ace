"""
trainer.py

Trainer is the class representing the trainer mode.
Makes use of SlideGen class for generating and viewing slides
"""

from PyQt4 import QtGui, QtCore
from slide_gen import SlideGen
from slide_scene import SlideScene
from enum import ModeEnum
from session import Session, Estimate
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
        and focus controls for the slide. These are all grouped into a single
        layout and returned to the initUI function.
    """
    def initSlideLayout(self):

        self.slide_scene = SlideScene(QtCore.QRectF(0,
                                                    0,
                                                    self.SLIDE_WIDTH,
                                                    self.SLIDE_HEIGHT), 
                                                    self) #trainer is parent
                                          
        #Build the view
        self.view = QtGui.QGraphicsView(self.slide_scene,
                                        self) #trainer is parent
        #Disable scroll bars
        self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        self.view.setSizePolicy(QtGui.QSizePolicy.Fixed,
                                QtGui.QSizePolicy.Fixed)        
    

        #build focus controls
        focus_text = QtGui.QLabel("Focus: ")
        self.focus_slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.focus_slider.setTickInterval(25)
        self.focus_slider.setSliderPosition((self.slide_scene.current_focus+1)*15)
        
        focus_plus_btn = QtGui.QPushButton("+")
        focus_minus_btn = QtGui.QPushButton("-")
        focus_plus_btn.setMaximumWidth(25)
        focus_minus_btn.setMaximumWidth(25)

        #Connect the focus buttons to the focus adjustment functions         
        focus_plus_btn.connect(focus_plus_btn, QtCore.SIGNAL("pressed()"),
                        self.slide_scene.focusUp)
        focus_minus_btn.connect(focus_minus_btn, QtCore.SIGNAL("pressed()"),
                        self.slide_scene.focusDown)
        
        self.focus_slider.valueChanged.connect(self.slide_scene.sliderFocus)

        #Group the focus controls into a layout.
        focus_layout = QtGui.QHBoxLayout()
        focus_layout.addWidget(focus_text)
        focus_layout.addWidget(focus_minus_btn)
        focus_layout.addWidget(focus_plus_btn)
        focus_layout.addWidget(self.focus_slider)
        
        # Group the slide view and focus layout into a
        # single layout for the slide.
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.view)
        layout.addLayout(focus_layout)
        
        return layout

    """
    QVBoxLayout self.initEstimateLayout():
        Called by self.initEstimateLayout() to build the range buttons, submission button,
        and feedback display for estimates.
    """
    def initEstimateLayout(self):
        widget = QtGui.QWidget(self)
        self.guess_group = QtGui.QButtonGroup(widget)

        #Create range selector buttons        
        for _range in range(Trainer.LOW_POW2, Trainer.HIGH_POW2+1):
            low = 2**_range
            high = 2*low -1
            btn_str = str(low)+"-"+str(high) 
            temp_btn = QtGui.QRadioButton(btn_str)
            
            #Add each button as a member of the class so it persists
            #These are created dynamically so that the minimum and maximum range
            # can be changed easily.
            member_name = "r"+str(_range)
            setattr(self, member_name, temp_btn);
            btn = getattr(self, member_name)
            self.guess_group.addButton( btn)
            self.guess_group.setId(btn, _range)
        
        #Set the first button checked to avoid undefined behavior when submitting
        # an estimate with no range selected.
        getattr(self,"r"+str(Trainer.LOW_POW2)).setChecked(True)
        
        #Create button to submit estimate.
        button = QtGui.QPushButton("Estimate Algae Count")
        button.connect( button, QtCore.SIGNAL("pressed()"),
                        self.submitEstimate)
        
        #Create estimate feedback display.
        self.estimate_display = QtGui.QTextEdit()
        self.estimate_display.setReadOnly(True)

        #Create Main Menu button
        menu_button  = QtGui.QPushButton("Main Menu")
        menu_button.connect(menu_button, QtCore.SIGNAL("pressed()"),
                        lambda: self.parent.changeMode(ModeEnum.MENU))

        #Create estimate number label
        self.estimate_label = QtGui.QLabel()      

        #Sub-layout that contains current slide number and main menu button
        estimate_top_layout = QtGui.QHBoxLayout()
        estimate_top_layout.addWidget(self.estimate_label)
        estimate_top_layout.addWidget(menu_button)
        
        #Organize the above elements into a single layout.
        estimate_layout = QtGui.QVBoxLayout()
        estimate_layout.addLayout(estimate_top_layout)
        estimate_layout.addWidget(self.estimate_display)
        buttons = self.guess_group.buttons()
        for btn in buttons:
            estimate_layout.addWidget(btn)
        estimate_layout.addWidget(button)
        
        return estimate_layout
    
    """
    submitEstimate():
        submitEstimate calculates data about the estimate, checks to
        see if it was the final estimate in the session, writes feedback
        to the estimate display, etc.
        
        This method is called by a signal connected to the submit
        button, not explicitly in code.

        **This method could benefit from being split into several functions.
    """    
    def submitEstimate(self):
        #Check which range was selected.
        pow2_range = self.guess_group.checkedId() 
        
        if (pow2_range):
            estimate = 2**pow2_range
        else:
            #This function was called without a valid range selected.
            return False

        #Gather data and calculate error of the estimate.
        estimate_range = str(estimate) + '-' + str(estimate * 2 - 1)

        actual = self.slide_scene.count()

        log_estimate = int(log(estimate, 2))
        log_actual = int(log(actual,2))

        low = 2**int(log(actual,2))
        actual_range = str(low) + '-' + str(low * 2 - 1)
        
        log_error = log_estimate - log_actual

        #Display feedback on the estimate in the estimate_display panel
        if log_error == 0:
            status = " - Correct!\n"
        else:
            status = " - Incorrect"
            if log_error < 0:   
                status += "\nYour estimate was too low.\n"
            else:
                status += "\nYour estimate was too high.\n"
            
        self.estimate_display.append(
                "\nSlide " + str(self.estimate_number) + status +
                "\nEstimate: " + estimate_range +
                "\nActual Range: " + actual_range +
                "\nExact Count: " + str(actual) +
                "\nLog Error: " + str(log_error) + "\n")

        #Add the estimate to the current_session list.
        this_estimate = Estimate(estimate, actual)
        self.current_session.addEstimate(this_estimate)

        
        self.current_session.error_sum += fabs(log_error)
        self.current_session.total_estimates += 1
        bias = 7
        self.current_session.log_err_list[log_error+bias] += 1
        
        #Save thumbnail of estimate to disk.
        filename = "thum_"+str(int(round(time.time())))+"_"+str(self.estimate_number)+".png"
        imagePath = os.path.normpath("./session/"+filename)
        self.current_session.addImage(self.slide_scene.save_image(imagePath, 100, 100))

        #update display            
        self.estimate_label.setText("Slide " +  str(self.estimate_number) + "/" + str(self.num_slides))
        if (not self.current_session.isComplete() ):
            self.slide_gen.genSlide(self.slide_scene)
            self.estimate_number += 1
                       
        else:
            #Send the session information to the stats page.
            self.stats_ref.recordSession(self.current_session)
            
            #Display the stats for the session
            session_error = self.current_session.error_sum / self.num_slides
            
            self.estimate_display.append("\nSession complete!")
            self.estimate_display.append("Average log error for this session: " + 
                                            "{:.2f}".format(session_error) + "\n")

            #MessageBox - ask the user if they wish to start another session
            self.endMessage = QtGui.QMessageBox.question(self,'Message',
                 "Session complete! Try again?",
                 QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)

            #Based on the user decision, start a new session or go to main menu.
            if self.endMessage == QtGui.QMessageBox.Yes:
                self.startNewSession()
            elif self.endMessage == QtGui.QMessageBox.No:
                self.has_active_session = False
                self.parent.changeMode(ModeEnum.MENU)

    """
    bool startNewSession():
        Attempts to start a new session with a user defined number of slides.
        Returns True if a new session was started,
        returns False if a session was not started (due to user clicking 'Cancel')
    """
    def startNewSession(self):
        self.estimate_sum = 0
        self.actual_sum = 0
        self.estimate_number = 1

        #Ask user for number of slides desired in next session
        #   only accepts values between 1 and self.max_session_length
        self.num_slides, ok = QtGui.QInputDialog.getInt(self, 'Trainer', 
            'How many algae slides would you like to generate?',
            10, 1, self.max_session_length)

        if ok:
            self.has_active_session = True
            #Write initial estimate_label
            self.estimate_label.setText("Slide 1/" +
                str(self.num_slides))
            
            self.estimate_display.append("Beginning new session...")

            #Have slide_gen generate a new slide
            self.slide_gen.genSlide(self.slide_scene)
            self.current_session = Session(self.num_slides)
            self.focus_slider.setSliderPosition((self.slide_scene.current_focus+1)*15)
            return True
        else:
            self.has_active_session = False
            return False