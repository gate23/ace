#ifndef TRAINER_H
#define TRAINER_H

#include <QMainWindow>
#include "editor.h"

namespace Ui {
class trainer;
}

class trainer : public QMainWindow
{
    Q_OBJECT

public:
    explicit trainer(QWidget *parent = 0);
    ~trainer();

private:
    Ui::trainer *ui;
    editor e;


private slots:
    void mainMenuClicked();

};

#endif // TRAINER_H
