# -*- coding: utf-8 -*-
# @Time     : 2020/7/28 14:07
# @Author   : Zhili
# @FileName : input_code.py
# @Software : PyCharm


def input_code(driver, code):
    l1 = list(code)
    dict_data = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16}
    for i in l1:
        if dict_data.get(i):
            driver.press_keycode(dict_data[i])
        else:
            print('error')
