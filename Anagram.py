#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 18:40:52 2019

@author: priyanka
"""
def anagrams(file):
	userInput = input("Enter the word to find anagrams-")
	userInput = userInput.lower()
	print("Word used to find anagrams is - {}".format(userInput))
	lists = open(file).read().splitlines()
	sort_words = sorted(userInput)
	anagram = []
	for word in lists:
		word = word.lower()
		if(sorted(word) == sort_words):
		   anagram.append(word)
	print()	   
	if len(anagram) == 0:
		   print("Cannot find the word in the file. Try another word!")
	else:
		   print("Anagrams for the word =", *anagram, sep='\n')
           
           
file = str("English") + str('.txt')
anagrams(file)     