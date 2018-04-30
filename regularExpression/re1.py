import re
str1 = 'imooc python'
#print str1.startswith('im')

pa = re.compile(r'imooc')
ma = pa.match(str1)
print ma.string

pa1 = re.compile(r'_')
ma1 = pa1.match('_ss')
print ma1.group()