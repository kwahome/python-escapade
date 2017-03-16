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

def highest_product(int_list):

	result = [0] * len(int_list)

	# for each integer, we find the product of all the integers
    # before it, storing the total product so far each time

	product = 1
	i = 0
	while i < len(int_list):
		result[i] = product
		product *= int_list[i]
		i += 1

	# for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers

	product = 1
	i = len(int_list) - 1
	while i >= 0:
		result[i] *= product
		product *= int_list[i]
		i -= 1

	return result

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
	print highest_product(integers)

	print "\n"

if __name__ == "__main__":
	
	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
