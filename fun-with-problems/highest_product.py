# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Highest product from three integers in a list
# Project: python-escapade
# Package: fun-with-problems
#
#
# Given a list of integers, find the highest product you can get from three of the integers.
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

def highest_product(int_list):

	int_list = merge_sort(int_list,"desc")

	return int_list[0] * int_list[1] * int_list[2]

def main():

	integers = []
	proceed = False

	print "Highest product from three integers in a list"
	print "---------------------------------------------"

	while proceed is False:
		number = input("Enter the number of integers in the list ")
		if number > 3: proceed = True
		else: print "Getting the highest product of 3 integers in a int_list requires at least 3 integers"
		print "\n"

	for i in range (1,number+1):
		integers_value = input("Please enter integer "+str(i)+": ")
		integers.append(integers_value)

	print "\n"
	print "Entered list of integers: "
	print integers
	print "\n"

	print "Product of every integer in the list except the integer at that index:"
	print "\n"
	print highest_product(integers)

	print "\n"

if __name__ == "__main__":
	
	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
