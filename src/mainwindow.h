#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QPushButton>
#include "trainer.h"
//#include <QLabel>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private:
    Ui::MainWindow *ui;

    /* Label to add to status bar */
  //  QLabel *statusLabel;
    QPushButton *pushButton;
    trainer t;

private slots:
    void button1Clicked();
    void button2Clicked();
};


#endif // MAINWINDOW_H
