# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Finding the product of every integer in a list except the integer at the current index
# Project: python-escapade
# Package: fun-with-problems
#
#
# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
#
# For example, given: 
# 
# [1, 7, 3, 4]
#
# your function would return:
# 
# [84, 12, 28, 21]
#
# by calculating:
# 
# [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
#
# Do not use division in your solution.
#
#============================================================================================================================================

import sys

def twisted_product(int_list):

	result = [0] * len(int_list)

	# for each integer, we find the product of all the integers
    # before it, storing the total product so far each time

	product = 1
	i=0
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

	print "Product of every integer in a list except the integer at that index"
	print "-------------------------------------------------------------------"

	while proceed is False:
		number = input("Enter the number of integers in the list ")
		if number > 1: proceed = True
		else: print "Getting the product of integers at other indices requires at least 2 integers"
		print "\n"

	for i in range (1,number+1):
		integers_value = input("Please enter the integer "+str(i)+": ")
		integers.append(integers_value)

	print "\n"
	print "Entered list of integers: "
	print integers
	print "\n"

	print "Product of every integer in the list except the integer at that index:"
	print "\n"
	print twisted_product(integers)

	print "\n"

if __name__ == "__main__":
	
	# try:
	sys.exit(main())

	# except Exception:
	# 	print "An error has occured"
