"""
editor.py
Contains all the classes for edit mode

Update 8/20:
Added continuous flow w/o needing to move mouse.
Flow rate is adjustable.

Issues:
-Moving slider right decreases flow rate, left increases.
(should be the other way)

-Changing the flow rate is convoluted as fuck. The classes in
this module need to be rearranged.

"""
import time
from random import uniform
from PyQt4 import QtCore, QtGui

class Editor(QtGui.QWidget):
    def __init__(self, parent):
        super(Editor, self).__init__(parent)
        
        self.scene = GraphicsScene(self)
        
        display = QtGui.QGraphicsView(self.scene)
        
        bg_texture = QtGui.QPixmap('background.jpg')
        background = QtGui.QBrush(bg_texture)
        self.scene.setBackgroundBrush(background)
        
          
        #toolbar with editing tools
        self.toolbar = QtGui.QToolBar(self)
        #self.toolbar.setOrientation(QtCore.Qt.Vertical)
        
        
        #add the toolbar to the main window, but as a hidden toolbar
        self.parent().addToolBar(self.toolbar)
        self.toolbar.toggleViewAction().setChecked(False)
        self.toolbar.toggleViewAction().trigger()
        
        dropper = Dropper(self, self.scene) 
        self.toolbar.addWidget(dropper)
        
        
        test_action = QtGui.QAction(QtCore.QString('test'),self.toolbar)
        self.toolbar.addAction(test_action)
          
        self.layout = QtGui.QHBoxLayout()
        self.layout.addWidget(display)
        
        self.setLayout(self.layout)
                              
    
#QGraphicsScene is subclassed in order to override its mousePressEvent method        
class GraphicsScene(QtGui.QGraphicsScene):
    def __init__(self, parent):
        super(GraphicsScene, self).__init__(parent)
        
        self.setSceneRect( QtCore.QRectF(0,0,500,400) )
        
        self.texture = QtGui.QPixmap('aphanothece1.png')
        self.texture = self.texture.scaled( QtCore.QSize(15, 15) )
        
        self.time_placed = time.clock()
        self.flow_rate = 100 
        
        self.mouse_down = False
        self.mouse_pos = QtCore.QPointF(0,0)
        self.drop_timer = QtCore.QTimer(self)
        self.drop_timer.connect(    self.drop_timer,
                                    QtCore.SIGNAL("timeout()"),
                                    (lambda: self.addCellAtMouse(self.mouse_pos) )
                                )
    def print_timer(self):
        print "Timer done!"
    #Stores the mouse event as the mouse moves. (Only when mouse is held down)
    #Allows drop_timer to add cells at the current mouse position.
    def mouseMoveEvent(self, event):
        if (self.mouse_down == True):
            self.mouse_pos = QtCore.QPointF(event.scenePos() )
        
    def mousePressEvent(self, event):
        super(GraphicsScene, self).mousePressEvent(event)
        self.addCellAtMouse(QtCore.QPointF(event.scenePos()) )
        
        self.mouse_down = True
        self.mouse_event = event
        
        self.drop_timer.start(self.flow_rate)
           
    def mouseReleaseEvent(self, event):
        super(GraphicsScene, self).mouseReleaseEvent(event)
        
        self.mouse_down = False
        
        self.drop_timer.stop()
    
    
    #addCellAtMouse:
    #Adds a cell at the position of the mouse on the graphics scene.
    #Bugs: Position center is not corrected after rotation. 
    def addCellAtMouse(self, position):
        cell = QtGui.QGraphicsPixmapItem(self.texture)
 
        cell.setPos(position.x(), position.y() )
        
        rotation = uniform(0,359.9)
        cell.setRotation(rotation)
         
        self.addItem(cell)
        
    def setFlow(self,value):
        self.flow_rate = value
        
class Dropper(QtGui.QWidget):
    def __init__(self,parent,scene):
        super(Dropper, self).__init__(parent)
        self.setFixedWidth(100)
        self.scene_ref = scene
        
        label = QtGui.QLabel("Dropper")
        flow_label = QtGui.QLabel("Flow Rate")
        self.flow_control = QtGui.QSlider(QtCore.Qt.Horizontal)
        #min/max delays for dropping cells (in milliseconds)
        self.flow_control.setRange(25, 200)
        self.flow_control.setValue(100)
        
        self.flow_control.connect(  self.flow_control,
                                    QtCore.SIGNAL("sliderReleased()"),
                                    self.updateFlowRate
                            )
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(flow_label)
        layout.addWidget(self.flow_control)
        
        self.setLayout(layout)
    
    def updateFlowRate(self):
        self.scene_ref.setFlow( self.flow_control.value() )
        
    