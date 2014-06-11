from PyQt4 import QtCore, QtGui
from ACEUI import Ui_MainWindow
import slidegen
#pyuic4 ACE.ui > ACEUI.py   

#TODO Global variables - shouldn't be global?
guessNum = 1
currentSlide = None

#Click even for main menu Trainer button
def trainerButtonClicked():
    thisIndex = ui.stackedWidget.indexOf(ui.Trainer)
    ui.stackedWidget.setCurrentIndex(thisIndex)
    populateStatusbar()
    genColony()

#Click even for main menu Editor button
def editorButtonClicked():
    thisIndex = ui.stackedWidget.indexOf(ui.Editor)
    ui.stackedWidget.setCurrentIndex(thisIndex)
    populateStatusbar()
    genColony()

#Click even for main menu Statistics button
def statisticsButtonClicked():
    thisIndex = ui.stackedWidget.indexOf(ui.Statistics)
    ui.stackedWidget.setCurrentIndex(thisIndex)

#Click even for Main Menu button
def mainMenuClicked():
    thisIndex = ui.stackedWidget.indexOf(ui.MainPage)
    ui.stackedWidget.setCurrentIndex(thisIndex)
    ui.statusbar.hide()

def genColony():
    #Delete all 
    if (ui.verticalLayout_t_algae.count() > 0):
        for i in range(ui.verticalLayout_t_algae.count()): 
            ui.verticalLayout_t_algae.itemAt(i).widget().setParent(None)

    algaeThing = slidegen.SlideGen()
    ui.verticalLayout_t_algae.addWidget(algaeThing)

    #KILL THIS
    if (ui.verticalLayout_e_algae.count() > 0):
        for i in range(ui.verticalLayout_e_algae.count()): 
            ui.verticalLayout_e_algae.itemAt(i).widget().setParent(None)
    algaeThing2 = slidegen.SlideGen()
    ui.verticalLayout_e_algae.addWidget(algaeThing2)

    #Set to glboal
    global currentSlide
    currentSlide = algaeThing

def submitClicked(self):
    global guessNum
    global currentSlide

    actualNum = currentSlide.cell_count
    
    guessStr = ui.textEdit_t_guess.toPlainText()
    #check for valid guess - doesn't check for just numbers
    if str(guessStr).isdigit():
        #calculations
        margin = int(guessStr) - actualNum
        errorPct = float(margin) / float(actualNum)

        #Add guess string to edit text
        ui.textEdit_t_guess.setText("")
        ui.textEdit_t_output.append("Slide " + str(guessNum))
        ui.textEdit_t_output.append("Guessed: " + guessStr)
        ui.textEdit_t_output.append("Actual: " + str(actualNum))
        ui.textEdit_t_output.append(str(margin) + " (%2f" % errorPct + "%) off\n")

        #Change slide number
        guessNum += 1
        ui.label_t_slide_num.setText("Slide " + str(guessNum) + " / 10")

        #generate new one
        genColony()
    else:
        errorMsg = QtGui.QMessageBox.warning(ui.pushButton_t_submit,"Error",\
                    "Invalid guess",QtGui.QMessageBox.Ok,QtGui.QMessageBox.NoButton)


#Connect each event to buttons
def connectActions():
    #Main menu button actions
    ui.pushButton_mm_editor.clicked.connect(editorButtonClicked)
    ui.pushButton_mm_trainer.clicked.connect(trainerButtonClicked)
    ui.pushButton_mm_statistics.clicked.connect(statisticsButtonClicked)
    ui.pushButton_mm_exit.clicked.connect(QtGui.qApp.quit)
    ui.actionClose.triggered.connect(QtGui.qApp.quit)

    #Buttons / menu options that return to main menu
    ui.pushButton_t_mm.clicked.connect(mainMenuClicked)
    ui.pushButton_e_mm.clicked.connect(mainMenuClicked)
    ui.pushButton_s_mm.clicked.connect(mainMenuClicked)
    ui.actionMain_Menu.triggered.connect(mainMenuClicked)
    
    ui.pushButton_t_submit.clicked.connect(submitClicked)

#Basic test thing to show 20x6 table
def testTable():
    ui.tableWidget_s.setRowCount(20)
    ui.tableWidget_s.setColumnCount(6)

#Fill statusbar with widgets (that are currently placed in Trainer... eh)
def populateStatusbar():
    #status bar is hidden elsewhere
    ui.statusbar.show()

    #status text
    ui.statusbar.addWidget(ui.label_t_status)
    
    #Vertical line seperator
    ui.statusbar.addWidget(ui.line_t_1)

    #focus stuff
    ui.statusbar.addWidget(ui.label_t_focus)
    ui.statusbar.addWidget(ui.pushButton_t_focus_minus)
    ui.statusbar.addWidget(ui.pushButton_t_focus_plus)

    #Another seperator
    ui.statusbar.addWidget(ui.line_t_2)

    #zoom stuff
    ui.statusbar.addWidget(ui.label_t_zoom)
    ui.statusbar.addWidget(ui.pushButton_t_zoom_minus)
    ui.statusbar.addWidget(ui.pushButton_t_zoom_plus)
 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    #connectactions events for UI
    ui.setupUi(MainWindow)
    #hide status bar
    ui.statusbar.hide()
    connectActions()

    #This will be moved elsewhere later
    testTable()

    MainWindow.setGeometry(QtCore.QRect(10, 10, 1024,768))
    MainWindow.show()
    sys.exit(app.exec_())