# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Two eggs problem
# Project: python-escapade
# Package: fun-with-problems
#
#
# A building has 100 floors. One of the floors is the highest floor an egg can be dropped from without breaking.
#
# If an egg is dropped from above that floor, it will break. If it is dropped from that floor or below, it will be completely undamaged and 
# you can drop the egg again.
# 
# Given two eggs, find the highest floor an egg can be dropped from without breaking, with as few drops as possible.
#
#============================================================================================================================================

import sys
import operator
import math

def egg_drop(floors, eggs):

	assert 1 <= eggs <= floors, 'Building has floors from 1 through {}'.format(floors)

	delta = int (math.ceil((math.sqrt(1 + 8 * floors) -1)/eggs))

	low, high = 1, delta

	while low < floors:
		if high >= eggs:
			print(' |-> First egg broke on floor {}'.format(high))

			for i in range(low, high+1):
				if i >= eggs:
					print(' |-> Second egg broke on floor {}'.format(i))
					if i == 1:
						raise ValueError("Eggs will always break")
					else:
						return i - 1
		else:
			delta -= 1
			low, high = high, high + delta
			if high > floors:
				high = floors
	return floors

	# if eggs == 1 or floors == 0:
	# 	return floors

	# min_value = float("inf")

	# for floor in range(1, floors+1):
	# 	min_value = min(min_value, 1 + max(egg_drop(eggs-1, floor-1), egg_drop(eggs, floors - floor)))
	# return min_value

def main():

	proceed = False

	print "The Two Egg problem"
	print "----------------------"

	while proceed is False:
		floors = input("Enter the number of floors ")
		if floors > 0: proceed = True
		else: print "The two egg problem requires at least one floor"
		print "\n"

	proceed = False
	while proceed is False:
		eggs = input("Enter the number of eggs ")
		if eggs > 0: proceed = True
		else: print "The two egg problem requires at least one egg"
		print "\n"

	print "\n"
	print "Number of floors: " + str(floors)
	print "Number of eggs: " + str(eggs)
	print "\n"

	print "Highest floor an egg can be dropped from:"
	print "\n"
	print egg_drop(floors, eggs)

	print "\n"

if __name__ == "__main__":
	
	# try:
	sys.exit(main())

	# except Exception:
	# 	print "An error has occured"
