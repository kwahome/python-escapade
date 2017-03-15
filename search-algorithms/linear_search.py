# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Linear Search Algorithm
# Project: python-escapade
# Package: search-algorithms
#
#
# Linear search is a very simple search algorithm. In this type of search, a sequential search is made over all items one by one.
# Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data 
# collection.
#
# Algorithm:
# ----------
#
# Linear Search ( Array A, Value x)
#
#	Step 1: Set i to 1
#	Step 2: if i > n then go to step 7
#	Step 3: if A[i] = x then go to step 6
#	Step 4: Set i to i + 1
#	Step 5: Go to Step 2
#	Step 6: Print Element x Found at index i and go to step 8
#	Step 7: Print element not found
#	Step 8: Exit
#
# Pseudocode:
# -----------
#	procedure linear_search (list, value)
#
#   	for each item in the list
#
#      		if match item == value
#
#       	  return the item's location
#
#      		end if
#
#   	end for
#
#	end procedure
#
#============================================================================================================================================

import sys

def linear_search(search_list,key):

	i = 0

	for i in range(len(search_list)):
		if search_list[i] == key:
			return i
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

		search_result = linear_search(search_list,search_key)

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
