# 作者：倔强的瓜小黄
# 日期：2020/5/25 上午 09:34
# 工具：PyCharm
# Python版本：3.8.0
# -*- coding: utf-8 -*-
import math
import cmath
import time
import calendar
import re
import easygui as g  # 导入EasyGui模块

#敏感词文件字符串
senfile=""
senword=""
#读取含有敏感词的文件
# fileopenbox()函数的返回值是你选择的那个文件的具体路径
try:
    #用图形化打开此电脑,选择需要进行敏感词屏蔽的文件
    dataSource = g.fileopenbox('open file', 'C:/User/Administrator/Desktop/__pycache__')
    fo1 = open(dataSource, "r", encoding='UTF-8')
    for line in fo1.readlines():
        senfile += line
except IOError:
    print("Error:没有找到文件或读取文件失败！")
else:
    print("Success！")
    fo1.close()

#加载敏感词库
#屏蔽敏感词
try:
    fo2 = open("sen_advertisement.txt", "r+", encoding='utf-8')
    for line in fo2.readlines():
        line = line.strip()
        if senfile.find(line) >= 0:
            senfile = senfile.replace(line, "*" * len(line))
except IOError:
    print("Error:没有找到文件或读取文件失败！")
else:
    print("Success!")
    fo2.close()

#将过滤掉敏感词的文章写到一个新的文件中去
str=str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
try:
    fo = open(str + ".txt", "w",encoding='utf-8')
    fo.write(senfile)
except IOError:
    print("Error:没有找到文件或读取文件失败！")
else:
    print("Success！")
    fo.close()
