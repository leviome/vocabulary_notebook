# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(564, 230)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 50, 351, 41))
        self.textEdit.setObjectName("textEdit")
        self.input_word = QtWidgets.QPushButton(Dialog)
        self.input_word.setGeometry(QtCore.QRect(220, 140, 112, 34))
        self.input_word.setObjectName("input_word")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.input_word.setText(_translate("Dialog", "添加单词"))

