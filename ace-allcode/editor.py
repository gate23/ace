"""
editor.py
Contains classes for edit mode
"""
import time
from random import uniform
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os.path
from sprites import SpriteFactory, SpriteType
from slide import Slide

class Editor(QtGui.QWidget):
    def __init__(self, parent):
        super(Editor, self).__init__(parent)
        
        self.slide = EditorSlide(self)
        
        display = self.slide.view
        
        bgPath = os.path.normpath("./img/backgrounds/b2.png")
        bg_texture = QtGui.QPixmap(os.path.join(os.path.curdir, bgPath))
        background = QtGui.QBrush(bg_texture)
        #self.scene.setBackgroundBrush(background)
        
          
        #toolbar with editing tools
        self.toolbar = QtGui.QToolBar(self)
        #self.toolbar.setOrientation(QtCore.Qt.Vertical)
        
        
        #add the toolbar to the main window, but as a hidden toolbar
        self.parent().addToolBar(self.toolbar)
        self.toolbar.toggleViewAction().setChecked(False)
        self.toolbar.toggleViewAction().trigger()
        
        dropper = Dropper(self, self.slide.scene) 
        self.toolbar.addWidget(dropper)
        self.toolbar.addSeparator()
        
        depth_select = DepthSelect(self) 
        self.toolbar.addWidget(depth_select)
        self.toolbar.addSeparator()        
        
        test_action = QtGui.QAction(QtCore.QString('Another Tool'),self.toolbar)
        self.toolbar.addAction(test_action)
        self.toolbar.addSeparator()
          
        self.layout = QtGui.QHBoxLayout()
        self.layout.addWidget(display)
        
        self.setLayout(self.layout)
                              

class EditorSlide(Slide):
    def __init__(self, parent):
        super(EditorSlide, self).__init__(parent)
        
        self.scene = EditorScene(self)
        self.view.setScene(self.scene)
        
        background = QtGui.QBrush(self.bg_texture)
        self.scene.setBackgroundBrush(background)
        
#QGraphicsScene is subclassed in order to override its mousePressEvent method        
class EditorScene(QtGui.QGraphicsScene):
    def __init__(self, parent):
        super(EditorScene, self).__init__()
    
        self.slide_ref = parent
        
        self.time_placed = time.clock()
        self.flow_rate = 100 
        
        self.mouse_down = False
        self.mouse_pos = QtCore.QPointF(0,0)
        self.drop_timer = QtCore.QTimer(self)
        self.drop_timer.connect(    self.drop_timer,
                                    QtCore.SIGNAL("timeout()"),
                                    (lambda: self.addCellAtMouse(self.mouse_pos) )
                                )
                                
    #Stores the mouse event as the mouse moves. (Only when mouse is held down)
    #Allows drop_timer to add cells at the current mouse position.
    def mouseMoveEvent(self, event):
        if (self.mouse_down == True):
            self.mouse_pos = QtCore.QPointF(event.scenePos() )
        
    def mousePressEvent(self, event):
        super(EditorScene, self).mousePressEvent(event)
        self.addCellAtMouse(QtCore.QPointF(event.scenePos()) )
        
        self.mouse_down = True
        self.mouse_event = event
        
        self.drop_timer.start(self.flow_rate)
           
    def mouseReleaseEvent(self, event):
        super(EditorScene, self).mouseReleaseEvent(event)
        
        self.mouse_down = False
        
        self.drop_timer.stop()
    
    
    #addCellAtMouse:
    #Adds a cell at the position of the mouse on the graphics scene.
    #Bugs: Position center is not corrected after rotation. 
    def addCellAtMouse(self, position):
        deg_rotation = uniform(0.0,359.9)
        zvalue = 3         
        texture, rotation = self.slide_ref.get_texture(   int(SpriteType.APHANOTHECE_OUTLINE),
                                                zvalue, deg_rotation)

        cell = QtGui.QGraphicsPixmapItem(texture) 
        cell.setPos(position.x(), position.y() )
        cell.setRotation(rotation)
         
        self.addItem(cell)
        
    def setFlow(self,value):
        self.flow_rate = value
        
class DepthSelect(QtGui.QGroupBox):
    def __init__(self, parent):
        super(DepthSelect, self).__init__(parent)
        self.setFixedWidth(120)
        self.setTitle("Select Depth")     
        self.d1RadioButton = QRadioButton("Depth1")
        self.d1RadioButton.setChecked(True)
        self.d2RadioButton = QRadioButton("Depth2")
        self.d3RadioButton = QRadioButton("Depth3")
 
        radioLayout = QVBoxLayout()
        self.depth_group = radioLayout
        
        radioLayout.addWidget(self.d1RadioButton)
        radioLayout.addWidget(self.d2RadioButton)
        radioLayout.addWidget(self.d3RadioButton)
        self.setLayout(radioLayout)
                
        
class Dropper(QtGui.QGroupBox):
    def __init__(self,parent,scene):
        super(Dropper, self).__init__(parent)
        self.setFixedWidth(240)
        self.scene_ref = scene
        self.setTitle("Dropper")
        #flow_label = QtGui.QLabel("Flow Rate")
        high_label = QtGui.QLabel("High")
        low_label = QtGui.QLabel("Low")
        self.flow_control = QtGui.QSlider(QtCore.Qt.Horizontal)
        #min/max delays for dropping cells (in milliseconds)
        self.flow_control.setRange(25, 200)
        self.flow_control.setValue(100)
        
        self.flow_control.connect(  self.flow_control,
                                    QtCore.SIGNAL("sliderReleased()"),
                                    self.updateFlowRate
                            )
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(high_label)
        layout.addWidget(self.flow_control)
        layout.addWidget(low_label)
        
        #layout = QtGui.QVBoxLayout()
        #layout.addWidget(flow_label)
        #layout.addWidget(self.flow_control)
        
        self.setLayout(layout)
    
    def updateFlowRate(self):
        self.scene_ref.setFlow( self.flow_control.value() )