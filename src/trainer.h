#ifndef TRAINER_H
#define TRAINER_H

#include <QMainWindow>

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
};

#endif // TRAINER_H
