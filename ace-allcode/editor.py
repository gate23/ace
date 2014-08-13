"""
editor.py
Contains all the class for edit mode
*Super basic at the moment
"""

from PyQt4 import QtCore, QtGui

class Editor(QtGui.QWidget):
    def __init__(self, parent):
        super(Editor, self).__init__(parent)
        
        self.scene = GraphicsScene(self)
        
        display = QtGui.QGraphicsView(self.scene)
        
        bg_texture = QtGui.QPixmap('background.jpg')
        background = QtGui.QBrush(bg_texture)
        self.scene.setBackgroundBrush(background)
        
        self.cell_texture = QtGui.QPixmap('aphanothece1.png')
          
        #toolbar with editing tools
        self.toolbar = QtGui.QToolBar(self)
        
        #add the toolbar to the main window, but as a hidden toolbar
        self.parent().addToolBar(self.toolbar)
        self.toolbar.toggleViewAction().setChecked(False)
        self.toolbar.toggleViewAction().trigger()
        
        dropperAction = QtGui.QAction( QtCore.QString("Single Dropper"), self.toolbar)
        
        self.toolbar.addAction(dropperAction)
          
        self.layout = QtGui.QHBoxLayout()
        self.layout.addWidget(display)
        
        self.setLayout(self.layout)
                              
    
#QGraphicsScene is subclassed in order to override its mousePressEvent method        
class GraphicsScene(QtGui.QGraphicsScene):
    def __init__(self, parent):
        super(GraphicsScene, self).__init__(parent)
        
        self.setSceneRect( QtCore.QRectF(0,0,540,530) )
        
        self.texture = QtGui.QPixmap('aphanothece1.png')
        
    def mousePressEvent(self, event):
        super(GraphicsScene, self).mousePressEvent(event)
        cell = QtGui.QGraphicsPixmapItem(self.texture)
        position = QtCore.QPointF(event.scenePos()) - cell.boundingRect().center()
        cell.setPos(position.x(), position.y() )
        self.addItem(cell)