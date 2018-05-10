# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:24:42 2018

@author: Administrator
"""

import heapq

nums= [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))