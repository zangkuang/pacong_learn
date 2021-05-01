# -*- coding: utf-8 -*-
# author:lyz
# time:2021/4/26  20:58 
# tool：PyCharm

import re

# match = re.match(r'[1-9]\d{5}',"BIT 100081")
match = re.findall(r'[1-9]\d{5}','BIT100081 TSU100086')     #findall以列表类型返回全部能匹配的子串
"""if match:
    print(match)"""

# re.split()
"""splt = re.split(r'[1-9]\d{5}','BIT100081 TST100084',maxsplit=1) #maxsplit最大分割数，默认为0，即全部分割
print(splt)"""

# re.finditer() 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
"""match = re.finditer(r'[1-9]\d{5}','BIT100081 TSU100086')
for m in match:
    print(m.group(0))"""

#re.sub(pattern,repl,string,count=0,flags=0)
'''
在一个字符串中替换所有匹配正则表达式的子串返回替换后的字符串
pattern:正则表达式的字符串或原生字符串表示∙ 
repl:替换匹配字符串的字符串∙ 
string:待匹配字符串∙ 
count:匹配的最大替换次数∙ 
flags:正则表达式使用时的控制标记
'''
"""match = re.sub(r'[1-9]\d{5}','lyzcool','BIT100081 TSU100086',count=0)
print(match)"""

#re库的另一种等价用法
"""pat = re.compile(r'[1-9]\d{5}')
# rst = pat.search('BAT100086')
rst = re.search(r'[1-9]\d{5}','BAT100086')
print(rst.group(0))"""

#match对象属性及方法
"""match = re.search(r'[1-9]\d{5}','BAT100086 LYZ520520')
print(match.string)     #待匹配的字符串
print(match.re)         #正则
print(match.pos)        #字符串开始匹配起点
print(match.endpos)     #结束匹配点
print(match.group(0))   #匹配结果
print(match.start())    #匹配字符串在原始字符串的开始位置
print(match.end())      #匹配字符串在原始位置的结束位置
print(match.span())     #返回（.start(),end())"""

#re库的贪婪匹配和最小匹配
"""
#贪婪匹配
match = re.search(r'PY.*N','PYANBNCNDN')
print(match.group(0))       #默认采用贪婪匹配，输出匹配最长的子串"""
#最小匹配
match = re.search(r'PY.+？*N','PYANBNCNDN')       #？匹配前一个字符0次或1次
print(match.group(0))