# coding=utf-8
import re

ma = re.match(r'[\w]{4,10}@163.com$','ccjy5130@163.com');
print ma.group()

ma = re.match(r'\Aimooc[\w]*','imoocpython')
print ma.group()