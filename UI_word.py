#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: liaoliwei
@contact: levio@pku.edu.cn
@file: UI_word.py
@time: 2018/4/27 22:03
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from word import Ui_Dialog
from Topfile import Top_file


class Dialog(QDialog, Ui_Dialog):
	def __init__(self, parent=None):
		super(Dialog, self).__init__(parent)
		self.setupUi(self)

	@pyqtSlot()
	def on_input_word_clicked(self):
		pe = self.textEdit.toPlainText()
		res_type, times = Top_file(pe)
		if res_type:
			res_str = '单词:'+ pe + ' 为新添加单词！'
			QMessageBox.information(self, u'提示', res_str)
		else:
			res_str = ('单词:'+ pe + ' 已重复记录 ' +
					   str(int(times))+' 次！')
			QMessageBox.information(self, u'提示',res_str)


if __name__ == '__main__':
	import sys

	app = QtWidgets.QApplication(sys.argv)
	# Dialog = QtWidgets.QDialog()
	app.processEvents()
	ui = Dialog()
	# ui.setupUi(Dialog)
	ui.show()
	sys.exit(app.exec_())
