# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Quick Sort Algorithm
# Project: python-escapade
# Package: sorting-algorithms
#
# Quick sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays. 
# A large array is partitioned into two arrays one of which holds values smaller than the specified value, say pivot, based on which the 
# partition is made and another array holds values greater than the pivot value.
#
# Quick sort partitions an array and then calls itself recursively twice to sort the two resulting subarrays. 
# This algorithm is quite efficient for large-sized data sets as its average and worst case complexity are of Ο(n2), where n is the number 
# of items.
#
# Algorithm:
# ----------
#
#	Step 1 − Make the right-most index value pivot
#	Step 2 − partition the array using pivot value
#	Step 3 − quicksort left partition recursively
#	Step 4 − quicksort right partition recursively
#
# Pseudocode:
# ----------
#
#	procedure quickSort(left, right)
#
#		if right-left <= 0
#	   		return
#   	else     
#       	pivot = A[right]
#       	partition = partitionFunc(left, right, pivot)
#       	quickSort(left,partition-1)
#       	quickSort(partition+1,right)    
#    	end if		
#   
# 	end procedure
#
#============================================================================================================================================

import sys
import operator

def quick_sort(sort_list,order):

	if order == "asc":
		op = operator.lt
		# inverse of the operator assigned
		op_i = operator.gt
	elif order == "desc":
		op = operator.gt
		# inverse of the operator assigned
		op_i = operator.lt

	if len(sort_list) < 2:
		return sort_list
	else:
		top = []
		pivot_list = []
		bottom = []
		pivot = sort_list[0]

        for i in sort_list:
            if op(i, pivot):
                top.append(i)
            elif op_i(i, pivot):
                bottom.append(i)
            else:
                pivot_list.append(i)

        # recursively sort the top
        top = quick_sort(top,order)
        # recursively sort the bottom
        bottom = quick_sort(bottom,order)

        # combine the sorted top, pivot and bottom lists
        return top + pivot_list + bottom

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
	print quick_sort(items_list,order.lower())
	print "\n"

if __name__ == "__main__":
	
	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
