from PyQt4 import QtCore, QtGui
from ACEUI import Ui_MainWindow
#pyuic4 ACE.ui > ACEUI.py


#NOTE: I couldn't get this to work using 'self'... dunno if using 'ui' like this
#is the best idea but hey neat it works
def trainerButtonClicked():
    thisIndex = ui.stackedWidget.indexOf(ui.Trainer)
    ui.stackedWidget.setCurrentIndex(thisIndex)

def editorButtonClicked():
    thisIndex = ui.stackedWidget.indexOf(ui.Editor)
    ui.stackedWidget.setCurrentIndex(thisIndex)

def mainMenuClicked():
    thisIndex = ui.stackedWidget.indexOf(ui.MainPage)
    ui.stackedWidget.setCurrentIndex(thisIndex)

def statisticsButtonClicked():
    thisIndex = ui.stackedWidget.indexOf(ui.Statistics)
    ui.stackedWidget.setCurrentIndex(thisIndex)

def connectActions(ui):
    ui.pushButton_mm_editor.clicked.connect(editorButtonClicked)
    ui.pushButton_mm_trainer.clicked.connect(trainerButtonClicked)
    ui.pushButton_mm_statistics.clicked.connect(statisticsButtonClicked)
    ui.pushButton_mm_exit.clicked.connect(QtGui.qApp.quit)

    #YO I ADDED MAIN MENU BUTTONS WOO
    ui.pushButton_t_mm.clicked.connect(mainMenuClicked)
    ui.pushButton_e_mm.clicked.connect(mainMenuClicked)
    ui.actionMain_Menu.triggered.connect(mainMenuClicked)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    #connectactions events for UI
    ui.setupUi(MainWindow)    
    connectActions(ui) 
    MainWindow.setGeometry(QtCore.QRect(10, 10, 1024,728))
    MainWindow.show()
    sys.exit(app.exec_())