# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Selection Sort Algorithm
# Project: python-escapade
# Package: sorting-algorithms
#
# Selection sort is a simple sorting algorithm. 
# This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left 
# end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire list.
#
# The smallest element is selected from the unsorted array and swapped with the leftmost element, and that element becomes a part of the 
# sorted array. This process continues moving unsorted array boundary by one element to the right.
#
# This algorithm is not suitable for large data sets as its average and worst case complexities are of Ο(n2), where n is the number of items.
#
# Algorithm:
# ----------
#
#	Step 1 − Set MIN to location 0
#	Step 2 − Search the minimum element in the list
#	Step 3 − Swap with value at location MIN
#	Step 4 − Increment MIN to point to next element
#	Step 5 − Repeat until list is sorted
#
# Pseudocode:
# ----------
#
#	procedure selection sort 
#   	list  : array of items
#   	n     : size of list
#
#   	for i = 1 to n - 1
#   	/* set current element as minimum*/
#       	min = i    
#  
#       	/* check the element to be minimum */
#
#	       for j = i+1 to n 
#	          if list[j] < list[min] then
#	             min = j;
#	          end if
#	       end for
#
#	       /* swap the minimum element with the current element*/
#	       if indexMin != i  then
#	          swap list[min] and list[i]
#	       end if
#
#	    end for
#	
#	 end procedure
#
#============================================================================================================================================

import sys
import operator

def selection_sort(sort_list,sorting_order):

	if sorting_order == "asc":
		op = operator.lt
	elif sorting_order == "desc":
		op = operator.gt

	#we start loop at second element (index 1) since the first item is already sorted
	for i in range(0,len(sort_list)):

		# set current element position as minimum/maximum
		position = i

		# check whether the current element is indeed the minimum/maximum
		for j in range(i+1,len(sort_list)):
			if op(sort_list[j], sort_list[position]):
				position = j
        sort_list[i], sort_list[position] = sort_list[position], sort_list[i]
	return sort_list

def main():

	items_list = []

	number = input("How many items are in your list? ")
	print "\n"

	for i in range (1,number+1):
		list_item = raw_input("Please enter item "+str(i)+" in your list ")
		items_list.append(list_item)

	print "\n"
	print "Entered list: "
	print items_list
	print "\n"

	valid_order = False

	while valid_order != True:
		order = raw_input("In what order should the list be sorted? (Asc/Desc) ")
		print "\n"

		if order.lower() == "asc" or order.lower() == "desc":
			valid_order = True

	if order.lower() == "asc":
		order_name = "ascending"
	elif order.lower() == "desc":
		order_name = "descending"

	print "Sorted list in " + order_name + " order:"
	print selection_sort(items_list,order.lower())
	print "\n"

if __name__ == "__main__":
	
	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
