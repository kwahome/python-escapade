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

def egg_drop(floors, eggs):

	if floors is 1:
		return floors
		
	if eggs is 1:
		return floors

	return floors + eggs
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
