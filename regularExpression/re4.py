# coding=utf-8
import re

ma = re.match(r'abc|d','abc')
print ma.group()

ma = re.match(r'[1-9]?\d$','99')
print ma.group()
#|表示左右表达式都可以匹配
ma = re.match(r'[1-9]?\d$|100','100')
print ma.group()
#()表示分组
ma = re.match(r'[\w]{4,6}@(163|126).com','cjy51@126.com')
print ma.group()

ma = re.match(r'<[\w]+>','<book>')
print ma.group()
#\num引用之前的匹配的字符串
ma = re.match(r'<([\w]+>)[\w]+</\1','<book>python</book>')
print ma.group()

ma = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)','<book>Java</book>')
print ma.group()
