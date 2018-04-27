#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: liaoliwei
@contact: levio@pku.edu.cn
@file: Topfile.py
@time: 2018/4/27 16:17
"""
from . import read_excel
from xlutils.copy import copy
import os


def Top_file(input_word):
	filename = 'new_excels.xls'
	excel = read_excel.open_excel(filename)
	tables = read_excel.excel_table_byname(excel)
	word_list = excel.sheet_by_name(u'Sheet1').col_values(0)[1:-1]
	if input_word in word_list:
		word_index = word_list.index(input_word)
		times = tables[word_index]['Times']
		if times == '':
			content = 1
		else:
			content = times+1
		new_excel = copy(excel)
		new_excel.get_sheet(0).write(word_index+1, 1, content)
		new_excel.save('new_excels.xls')
		return False, content
	else:
		word_num = len(word_list)
		new_excel = copy(excel)
		new_excel.get_sheet(0).write(word_num + 2, 0, input_word)
		new_excel.save('new_excels.xls')
		return True, 0
