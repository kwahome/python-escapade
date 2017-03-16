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

def highest_product_of_3(int_list):
	max_number = max(int_list[0], int_list[1])
	min_number = min(int_list[0], int_list[1])
	highest_product_of_2 = int_list[0] * int_list[1]
	lowest_product_of_2 = int_list[0] * int_list[1]
	highest_product_of_3 = int_list[0] * int_list[1] * int_list[2]
	
	# Start with third integer; integer at index 2
	i = 2

	while i < len(int_list):
		highest_product_of_3 = max(highest_product_of_2 * int_list[i], lowest_product_of_2 * int_list[i], highest_product_of_3)
		lowest_product_of_2 = min(min_number * int_list[i],lowest_product_of_2)
		highest_product_of_2 = max(max_number * int_list[i],highest_product_of_2)
		max_number = max(max_number, int_list[i])
		min_number = min(min_number, int_list[i])
		i += 1

	return highest_product_of_3

def main():

	integers = []
	proceed = False

	print "Highest product from three integers in a list"
	print "---------------------------------------------"

	while proceed is False:
		number = input("Enter the number of integers in the list ")
		if number > 3: proceed = True
		else: print "Getting the highest product of 3 integers in a list requires at least 3 integers"
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
	print highest_product_of_3(integers)

	print "\n"

if __name__ == "__main__":
	
	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
