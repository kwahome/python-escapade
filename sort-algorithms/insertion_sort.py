# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Insertion Sort Algorithm
# Project: python-escapade
# Package: sorting-algorithms
#
# This is an in-place comparison-based sorting algorithm. Here, a sub-list is maintained which is always sorted. 
# For example, the lower part of an array is maintained to be sorted. 
# An element which is to be 'insert'ed in this sorted sub-list, has to find its appropriate place and then it has to be inserted there. 
# Hence the name, insertion sort. 
#
# The array is searched sequentially and unsorted items are moved and inserted into the sorted sub-list (in the same array). 
# This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2), where n is the number of items.
#
# Algorithm:
# ----------
#
#	Step 1 − If it is the first element, it is already sorted. return 1;
#	Step 2 − Pick next element
#	Step 3 − Compare with all elements in the sorted sub-list
#	Step 4 − Shift all the elements in the sorted sub-list that is greater than the 
#         value to be sorted
#	Step 5 − Insert the value
#	Step 6 − Repeat until list is sorted
#
# Pseudocode:
# ----------
#
#	procedure insertionSort( A : array of items )
#	   int holePosition
#	   int valueToInsert
#	
#	   for i = 1 to length(A) inclusive do:
#	
#	      /* select value to be inserted */
#	      valueToInsert = A[i]
#	      holePosition = i
#      
#	       /*locate hole position for the element to be inserted */
#		
#	       while holePosition > 0 and A[holePosition-1] > valueToInsert do:
#	          A[holePosition] = A[holePosition-1]
#	          holePosition = holePosition -1
#	       end while
#		
#	       /* insert the number at hole position */
#	       A[holePosition] = valueToInsert
#      
#	    end for
#	
#	end procedure
#
#============================================================================================================================================

import sys
import operator

def insertion_sort(sort_list,order):

	if order == "asc":
		op = operator.gt
	elif order == "desc":
		op = operator.lt

	if len(sort_list) < 2:
		return sort_list

	else:
		#we start loop at second element (index 1) since the first item is already sorted
		for i in range(1,len(sort_list)):
			# save the item
			value = sort_list[i]

	        # save the current position of the item
	        position = i

	        # while the item is not the first item and is smaller or greater than the item to it's left:
	        while position > 0 and op(sort_list[position-1], value):
	        	# the item overwrites the item to the left
	            sort_list[position] = sort_list[position-1]
	            # And we move on to the next position
	            position -= 1

	        # When we have found the right position (meaning the while loop is false)
	        # put the item in its correct spot in the list
	        sort_list[position] = value
	        
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
	print insertion_sort(items_list,order.lower())
	print "\n"

if __name__ == "__main__":
	
	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
