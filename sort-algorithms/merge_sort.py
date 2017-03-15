# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Merge Sort Algorithm
# Project: python-escapade
# Package: sorting-algorithms
#
# Merge sort is a sorting algorithm based on divide and conquer technique. 
# With worst-case time complexity being Ο(n log n), it is one of the most respected algorithms. 
#
# Algorithm:
# ----------
#
# Merge sort keeps on dividing the list into equal halves until it can no more be divided. 
# By definition, if it is only one element in the list, it is sorted. 
# Then, merge sort combines the smaller sorted lists keeping the new list sorted too.
#
#	Step 1 − if it is only one element in the list it is already sorted, return.
#	Step 2 − divide the list recursively into two halves until it can no more be divided.
#	Step 3 − merge the smaller lists into new list in sorted order.
#
# Pseudocode:
# ----------
#
#	procedure mergesort( var a as array )
#		if ( n == 1 ) return a
#
# 		var l1 as array = a[0] ... a[n/2]
# 		var l2 as array = a[n/2+1] ... a[n]
#
# 		l1 = mergesort( l1 )
# 		l2 = mergesort( l2 )
#
# 		return merge( l1, l2 )
# 	end procedure
#
# 	procedure merge( var a as array, var b as array )
#
# 		var c as array
#
# 		while ( a and b have elements )
# 	  		if ( a[0] > b[0] )
# 	     		add b[0] to the end of c
# 	     		remove b[0] from b
# 	  		else
# 	     		add a[0] to the end of c
# 	     		remove a[0] from a
# 	  		end if
# 		end while
#
# 		while ( a has elements )
# 	  		add a[0] to the end of c
# 	  		remove a[0] from a
# 		end while
#
# 		while ( b has elements )
# 	  		add b[0] to the end of c
# 	  		remove b[0] from b
# 		end while
#
# 		return c
#
# 	end procedure
#
#============================================================================================================================================

import sys
import operator

def merge(left,right,operator):
	"""Function to perform a two way merge"""
	if not len(left) or not len(right):
		return left or right

	merged = []
	
	i, j = 0, 0

	while (len(merged) < len(left) + len(right)):
		if operator(left[i], right[j]):
			merged.append(left[i])
			i+= 1
		else:
			merged.append(right[j])
			j+= 1

		if i == len(left) or j == len(right):
			merged.extend(left[i:] or right[j:])
			break
	return merged

def merge_sort(sort_list,sorting_order):
	"""Recersive merge sort function that divides the list into left and right halves"""
	if sorting_order == "asc":
		op = operator.lt
	elif sorting_order == "desc":
		op = operator.gt

	if len(sort_list) < 2:
		return sort_list

	else:
		middle = len(sort_list)/2

    	left_half = merge_sort(sort_list[:middle],sorting_order)
    	right_half = merge_sort(sort_list[middle:],sorting_order)

    	return merge(left_half,right_half, op)

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
	print merge_sort(items_list,order.lower())
	print "\n"

if __name__ == "__main__":
	
	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
