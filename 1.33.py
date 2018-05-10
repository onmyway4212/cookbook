# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:08:48 2018

@author: Administrator
"""
from collections import deque
#创建了一个固定长度的队列deque(maxlen=3)
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)