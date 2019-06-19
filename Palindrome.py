#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 18:53:58 2019

@author: priyanka
"""

def palindrome(file):
    lists = open(file).read().splitlines()
    for i in range(0, len(lists)):
        if str(lists[i]).lower() == str(lists[i]).lower()[::-1]:
            print(str(lists[i]))
            #To extract all palindrome and save to new file---
			#filenew = open('Palindrome.txt','a+')
			#filenew.write(str(lists[i] + '\n'))
			#filenew.close()
file = str("English") + str('.txt')
palindrome(file)
			