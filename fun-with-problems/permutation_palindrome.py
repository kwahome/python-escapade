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

def find_permutation_palindrome(string):
	# Dictionary to hold character frequencies
	frequency = {}

	# Traverse through the string character by character
	for char in string:
		# If a character in the string has been counted already, remove the counted character from frequency
		# This means that for a palindrome to hold, we have to have the equal numbers of the same character
		if char in frequency:
			del frequency[char]
		else:
			frequency[char] = True

	# At most one character may appear once and the string has permutation palindromes
	return len(frequency) <= 1

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
	print find_permutation_palindrome(string)

	print "\n"

if __name__ == "__main__":
	
	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
