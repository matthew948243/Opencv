# -*- coding: utf-8 -*- 
# @Time : 2022/11/11 11:32
# @Author : KeJun 
# @File : Demo.py
# @IDE ：PyCharm
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Main
import OpenCv01 as op


class Demo(QMainWindow):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.ui = Main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(
            lambda: (
                op.func1()
            )
        )

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        op.Video()

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        op.imgsplit()

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        op.drawgeometry()

    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        op.addPic()

    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        op.flip()

    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        op.rotate()

    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        op.wrap()

    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        op.rotateM()

    @pyqtSlot()
    def on_pushButton_10_clicked(self):
        op.juanji()

    @pyqtSlot()
    def on_pushButton_11_clicked(self):
        op.lvobo()

    @pyqtSlot()
    def on_pushButton_12_clicked(self):
        op.suanzi()

    @pyqtSlot()
    def on_pushButton_13_clicked(self):
        op.fushi()

    @pyqtSlot()
    def on_pushButton_14_clicked(self):
        op.pengzhang()

    @pyqtSlot()
    def on_pushButton_15_clicked(self):
        op.kaibiyunsuan("1")

    @pyqtSlot()
    def on_pushButton_16_clicked(self):
        op.xingtaitidu()

    @pyqtSlot()
    def on_pushButton_17_clicked(self):
        op.dingmao()

    @pyqtSlot()
    def on_pushButton_18_clicked(self):
        op.heimao()

    @pyqtSlot()
    def on_pushButton_19_clicked(self):
        op.chazhaolunkuo(self)

    @pyqtSlot()
    def on_pushButton_20_clicked(self):
        op.duobianxingbijin()

    @pyqtSlot()
    def on_pushButton_21_clicked(self):
        op.tubao()

    @pyqtSlot()
    def on_pushButton_22_clicked(self):
        op.zuixiaowaijiejuxing()

    @pyqtSlot()
    def on_pushButton_23_clicked(self):
        op.zuidawaijiejuxing()

    @pyqtSlot()
    def on_pushButton_24_clicked(self):
        op.tuxiangjinzitagaosi()

    @pyqtSlot()
    def on_pushButton_25_clicked(self):
        op.tuxiangjinzitalapulasi()

    @pyqtSlot()
    def on_pushButton_26_clicked(self):
        op.tongjizhifangtu()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    mainwind = Demo()
    mainwind.show()
    sys.exit(qApp.exec_())
