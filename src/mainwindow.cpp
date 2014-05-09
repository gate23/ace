#include "mainwindow.h"
#include "editor.h"
#include "trainer.h"
#include <QApplication>

/* NOTE: I renamed trainer.ui to mainwindow.ui for this. */
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    /* Status label being added to status bar */
//    statusLabel = new QLabel(this);
//    statusLabel->setText("Status label");
//    ui->statusbar->addPermanentWidget(statusLabel);

    connect(ui->pushButton,SIGNAL(clicked()),this,SLOT(button1Clicked()));
    connect(ui->pushButton_2,SIGNAL(clicked()),this,SLOT(button2Clicked()));

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::button1Clicked(){
    t.show();
    this->close();
}

void MainWindow::button2Clicked(){
    e.show();
<<<<<<< HEAD
    this->hide();
=======
    this->close();
>>>>>>> 3c0883ed98d56db5875d9850a3d81e86ca3ed692
}
