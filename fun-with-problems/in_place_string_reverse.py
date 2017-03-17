# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Reversing a string in-place
# Project: python-escapade
# Package: fun-with-problems
#
#
# Write a function to reverse a string in-place 
#
# Since strings in Python are immutable ↴ , first convert the string into a list of characters, do the in-place reversal on that list, and 
# re-join that list into a string before returning it. This isn't technically "in-place" and the list of characters will cost O(n)O(n)O(n) 
# additional space, but it's a reasonable way to stay within the spirit of the challenge. If you're comfortable coding in a language with 
# mutable strings, that'd be even better!  
#
#============================================================================================================================================

import sys

def reverse_string(string):

	string = list(string)

	# walk towards the middle, from both sides
	for left in range(len(string) / 2):
		
		right = -left - 1
		
		# swap the front word and back word
		string[left], string[right] = \
			string[right], string[left]

	return ''.join(string)

def main():

	proceed = False

	print "Reversing a string with an in-place function"
	print "------------------------------------------"

	string = raw_input("Enter the string to reverse: ")

	print "\n"
	print "Original string: "
	print string
	print "\n"

	print "Reversed string:"
	print "\n"
	print reverse_string(string)

	print "\n"

if __name__ == "__main__":
	
	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
