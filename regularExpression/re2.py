# coding=utf-8
import re
#ma = re.match(r'.','1d')和ma = re.match(r'[0-9]','1d')都可以匹配到含有该字符开头的若干个字符
#[.]这种写法是错误的
#然而一旦外层有'['或者'{'和其他的特殊符号，则只能匹配含有该字符的一个字符，如r'{[abc]}'
ma = re.match(r'.','1d')
print ma.group()

ma = re.match(r'{.}','{a}')
print ma.group()

ma = re.match(r'{..}','{a2}')
print ma.group()

ma = re.match(r'{[abc]}','{b}')
print ma.group()

ma = re.match(r'{[a-z]}','{e}')
print ma.group()

ma = re.match(r'{[a-zA-Z]}','{A}')
print ma.group()

ma = re.match(r'{[a-zA-Z0-9]}','{6}')
print ma.group()

ma = re.match(r'{[\w]}','{6}')
print ma.group()
#\W可以匹配空格
ma = re.match(r'{[\W]}','{ }')
print ma.group()

ma = re.match(r'\[[a]\]','[a]')
print ma.group()

ma = re.match(r'\d','123c')
print ma.group()

ma = re.match(r'\D','dfs1')
print ma.group()

ma = re.match(r'\s','  ')
print ma.group()

ma = re.match(r'\S','s')
print ma.group()

ma = re.match(r'[A-Z][a-z]','AsD')
print ma.group()

ma = re.match(r'[A-Z][a-z]*','AswD')
print ma.group()
#变量命名规则
#加+号和*效果一样
#python命名规则正则表达式
ma = re.match(r"a[_a-zA-Z]+[_\w]*", 'aSwDff2')
print ma.group()

ma = re.match(r'[1-9]?[0-9]','09')
print ma.group()

ma = re.match(r'[a-zA-Z0-9]{5}','abcd1')
print ma.group()

ma = re.match(r'[a-zA-Z0-9]{6,10}@163.com','cjy12345@163.com')
print ma.group()
#非贪婪模式，尽可能少匹配，这里指尽可能不匹配（匹配0次）
ma = re.match(r'[0-9][a-z]*?','1bc')
print ma.group()
#??和*?功能一样，尽可能少匹配，即匹配0次
ma = re.match(r'[0-9][a-z]??','1bc')
print ma.group()

ma = re.match(r'[0-9][a-z]+?','1bc')
print ma.group()

