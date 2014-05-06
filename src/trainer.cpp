#include "trainer.h"
#include "ui_trainer.h"

trainer::trainer(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::trainer)
{
    ui->setupUi(this);
}

trainer::~trainer()
{
    delete ui;
}
