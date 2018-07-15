# coding=utf-8
import re

str1 = 'imooc video = 1000'
#find()返回字符串索引
print str1.find('1000')

info = re.search('\d+',str1)
print info.group()

str2 = 'c++=100,java=90,python=80'
#info = re.search('\d+',str2)
#findall()找到所有的满足正则的匹配结果
info = re.findall('\d+',str2)
print info

str3 = 'imooc videonum = 1000'
#sub()替换目标值
info = re.sub(r'\d+','1001',str3);
print info

str4 = "imooc:C C++ Java, Python"
print re.split(r':|,',str4)