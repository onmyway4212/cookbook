# -*- coding: utf-8 -*-
"""
Created on Thu May 10 14:43:37 2018

@author: Administrator
"""

from collections import deque

#参数lines是打开的文件，pattern是匹配的内容，history是查找过的行
def search(lines, pattern, history=5):
    #deque(maxlen=N)创建了一个固定长度的队列，当有新记录加入而队列已满时会自动移除最老的那条记录。
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            #返回值line是匹配的行，previous_lines是匹配之前的行
            yield line, previous_lines
        previous_lines.append(line)

if __name__=='__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, '工作那点事', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)