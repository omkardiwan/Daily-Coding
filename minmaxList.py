 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 18:47:17 2020

@author: omkar
"""

list1 =[]
number = int(input("Enter How many elements to be added to list"))
for i in range(number):
    value = int(input("Value to be added to the list"))
    list1.append(value)
    
list1.sort()
print("max", list1[-1])
print("min",list1[0])
