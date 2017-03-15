# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Binary Search Algorithm
# Project: python-escapade
# Package: search-algorithms
#
#
# Binary search works on sorted arrays. 
# Binary search begins by comparing the middle element of the array with the target value. 
# If the target value matches the middle element, its position in the array is returned. 
# If the target value is less than or greater than the middle element, the search continues in the lower or upper half of the array, 
# respectively, eliminating the other half from consideration.
#
# Procedure:
# ----------
#
# Given an array A of n elements with values or records A0 ... An−1, sorted such that A0 ≤ ... ≤ An−1, and target value T,
# the following subroutine uses binary search to find the index of T in A.
#
#   - Set L to 0 and R to n − 1.
#   - If L > R, the search terminates as unsuccessful.
#   - Set m (the position of the middle element) to the floor (the largest previous integer) of (L + R) / 2.
#   - If Am < T, set L to m + 1 and go to step 2.
#   - If Am > T, set R to m – 1 and go to step 2.
#   - Now Am = T, the search is done; return m.
#
# This iterative procedure keeps track of the search boundaries via two variables. 
# Some implementations may place the comparison for equality at the end of the algorithm, resulting in a faster comparison loop but costing 
# one more iteration on average.
#
#============================================================================================================================================


import sys

def binary_search(search_list,key):

	found = False

	L = 0
	R = len(search_list)-1

	while found == False:
		if L>R:
			return "unsuccessful"
		else:
			m = (L+R)/2

			if search_list[m] == key:
				return m
			elif search_list[m] < key:
				L = m+1
				found = False
			elif search_list[m] > key:
				R = m-1
				found = False


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

		search_result = binary_search(search_list,search_key)

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
