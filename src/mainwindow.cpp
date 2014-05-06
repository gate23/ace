#include "mainwindow.h"
#include "ui_mainwindow.h"

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

    ui->pushButton->setText("Test");
}

MainWindow::~MainWindow()
{
    delete ui;
}
