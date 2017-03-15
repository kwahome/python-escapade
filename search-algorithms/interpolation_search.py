# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Interpolation Search Algorithm
# Project: python-escapade
# Package: search-algorithms
#
#
# Interpolation search is an improved variant of binary search. 
# This search algorithm works on the probing position of the required value. 
# For this algorithm to work properly, the data collection should be in a sorted form and equally distributed.
#
# There are cases where the location of target data may be known in advance. 
# For example, in case of a telephone directory, if we want to search the telephone number of Morphius. 
# Here, linear search and even binary search will seem slow as we can directly jump to memory space where the names start from 'M' are stored.
#
# Procedure:
# ----------
#
# Interpolation search finds a particular item by computing the probe position. 
# Initially, the probe position is the position of the middle most item of the collection.
#
# If a match occurs, then the index of the item is returned. To split the list into two parts, we use the following method:
#
#	mid = Lo + ((Hi - Lo) / (A[Hi] - A[Lo])) * (X - A[Lo])
#
#	where −
#   	A    = list
#   	Lo   = Lowest index of the list
#   	Hi   = Highest index of the list
#   	A[n] = Value stored at index n in the list
#
# If the middle item is greater than the item, then the probe position is again calculated in the sub-array to the right of the middle item. 
# Otherwise, the item is searched in the subarray to the left of the middle item. This process continues on the sub-array as well until the 
# size of subarray reduces to zero.
#
# Runtime complexity of interpolation search algorithm is Ο(log (log n)) as compared to Ο(log n) of BST in favorable situations.
#
# Algorithm:
# ----------
#
# As it is an improvisation of the existing BST algorithm, we are mentioning the steps to search the 'target' data value index, 
# using position probing −
#
#	Step 1 − Start searching data from middle of the list.
#	Step 2 − If it is a match, return the index of the item, and exit.
#	Step 3 − If it is not a match, probe position.
#	Step 4 − Divide the list using probing formula and find the new midle.
#	Step 5 − If data is greater than middle, search in higher sub-list.
#	Step 6 − If data is smaller than middle, search in lower sub-list.
#	Step 7 − Repeat until match.
#
#============================================================================================================================================

import sys

#
# Function to get the distance beween two strings
# To find the "distance" between two strings, we to look at the first letter that is different between them and assign a numeric value to each,
# then take the difference.

def strintcomp(fstring,lstring):
	if fstring.isdigit() and lstring.isdigit() :
		return int(fstring) - int(lstring)
	else:
		number = min(len(fstring),len(lstring))
		lstring = list(lstring)
		fstring = list(fstring)

		for char in range(0,number):
			if(fstring[char] != lstring[char]):
				return ord(fstring[char]) - ord(lstring[char])

		if len(lstring)>len(fstring):
			return ord(lstring[number])
		elif len(fstring)>len(lstring):
			return ord(fstring[number])
		else:
			return 0

# def strtoint(string):

# 	if string.isdigit():
# 		return int(string)

# 	else:
# 		s = 0
# 		for char in string:
# 			if char.isdigit():
# 				s += int(char)
# 			else:
# 				s += ord(char)%96
# 	return s

def interpolation_search(search_list,key):

	Lo  =  0
   	Hi  =  len(search_list)-1

   	while Lo!=Hi:
			
		if Lo > Hi:
			return "unsuccessful"
		
		else:
			#strtoint(search_list[Hi]) - strtoint(search_list[Lo]))
			#strtoint(key) - strtoint(search_list[Lo])

			Mid = Lo + ((Hi - Lo) / (strintcomp(search_list[Hi],search_list[Lo]))) * (strintcomp(key,search_list[Lo]))

			if search_list[Mid] == key:
				return Mid
			elif search_list[Mid] < key:
				Lo = Mid+1
			elif search_list[Mid] > key:
				Hi = Mid-1

	if search_list[Lo] == key:
   		return Lo

   	else:
   		return "unsuccessful"

def main():

	search_list = []

	number = input("How many items are in your search list? ")
	print "\n"

	for i in range (1,number+1):
		search_list_item = raw_input("Please enter item "+str(i)+" in your search list ")
		search_list.append(search_list_item)

	print "\n"
	print "Entered list: "
	print search_list
	print "\n"

	# Sort the list
	search_list.sort()

	print "Sorted list (ascending order): "
	print search_list
	print "\n"

	search_again = "no"

	while search_again.lower() != "yes":
		search_key = raw_input("Please enter the item you want to search ")
		print "Item to search: "+str(search_key)

		search_result = interpolation_search(search_list,search_key)

		print "\n"

		if search_result is "unsuccessful":
			print str(search_key) + " was not found in the sorted search list"
		else:
			print str(search_key) + " found at position "+str(search_result)+" of the sorted search list"

		print "\n"

		search_again = raw_input("Do you want to end search? (Yes/No) ")

if __name__ == "__main__":
	
	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
