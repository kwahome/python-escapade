# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Permutation Palindrome
# Project: python-escapade
# Package: fun-with-problems
#
#
# Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome
#
# You can assume the input string only contains lowercase letters.
#
#  Examples:
#
#    "civic" should return True
#    "ivicc" should return True
#    "civil" should return False
#    "livci" should return False
# 
#
#============================================================================================================================================

import sys

def find_palindrome_permutation(string):

	string = list(string)

	permutation  = []

	# walk towards the middle, from both sides
	for left in range(len(string)):
		
		right = -left - 1

		if string[right] == string[left]:
			permutation.append(string[left])


	if len(permutation) is 0:
		return "False"
	else:
		return "The permuation '" + ''.join(permutation) + "' in the string is a palindrome"

def main():

	print "Palindrome in any permutation of a string"
	print "------------------------------------------"

	string = raw_input("Enter the string: ")

	print "\n"
	print "String input: "
	print string
	print "\n"

	print "Does the string contain any permutation that is a palindrome?"
	print "\n"
	print find_palindrome_permutation(string)

	print "\n"

if __name__ == "__main__":
	
	# try:
	sys.exit(main())

	# except Exception:
	# 	print "An error has occured"
