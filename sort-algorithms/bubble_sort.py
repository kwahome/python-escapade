# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Bubble Sort Algorithm
# Project: python-escapade
# Package: sorting-algorithms
#
# Bubble sort is a simple sorting algorithm. 
# This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if 
# they are not in order. 
# This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2) where n is the number of items.
#
# Algorithm:
# ----------
#
# We assume list is an array of n elements. We further assume that swap function swaps the values of the given array elements.
#
# begin BubbleSort(list)
#
#   for all elements of list
#      if list[i] > list[i+1]
#         swap(list[i], list[i+1])
#      end if
#   end for
#   
#   return list
#   
# end BubbleSort
#
# Pseudocode:
# ----------
#
#   Bubblesort is an elementary sorting algorithm. The idea is to imagine bubbling the smallest elements of a (vertical) array to the
#   top; then bubble the next smallest; then so on until the entire array is sorted. Bubble sort is worse than both insertion sort and
#   selection sort. It moves elements as many times as insertion sort (bad) and it takes as long as selection sort (bad). On the positive
#   side, bubble sort is easy to understand. Also there are highly improved variants of bubble sort.
#
#  0] For each element at index i from n to 0, loop:
#  1] For each element at index j, from n to i exclusive, loop:
#  2] If the element at j is less than that at j+1, swap them.
#
#============================================================================================================================================

import sys
import operator

def bubble_sort(items_list,order):

	if order == "asc":
		op = operator.gt
	elif order == "desc":
		op = operator.lt
	
	for i in range(len(items_list)-1,0,-1):

		for j in range (i):

			if op(items_list[j], items_list[j+1]):

				temp = items_list[j]
				items_list[j] = items_list[j+1]
				items_list[j+1] = temp

	return items_list

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
	print bubble_sort(items_list,order.lower())
	print "\n"

if __name__ == "__main__":
	
	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
