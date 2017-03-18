# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Balanced Brackets Search
# Project: python-escapade
# Package: balanced-brackets
#
# This is a simple program to check for balanced brackets in a string 
#
# Algorithm:
# ----------
#
# begin check_brackets(text, brackets_array)
#   
#	define an empty array balanced_array
#
#   for all characters of text
#      if character is in dictionary of brackets and is an opening bracket
#			if matching closing bracket is in the balanced_array
#				remove this matching closing bracket
#			else
#				add the opening bracket in to the balanced_array
#		else
#			if matching opening bracket is in the balanced_array
#				remove this matching opening bracket
#			else
#				add the closing bracket in to the balanced_array
#
#	if length of balanced_array is 0
#		return True
#	else
#		return False
#   
# end check_brackets
#
#============================================================================================================================================

import sys

brackets_array = ['(',')','{','}','<','>','[',']']

def check_brackets(string_input, brackets_array):

	balanced_array = []

	string_input = list(string_input)

	for char in string_input:
		if char in brackets_array:
			char_index = brackets_array.index(char)
			# All opening brackets are at even positions in the brackets_array
			if char_index % 2 is 0:
				# if encountered character is an opening bracket, check for matching closing bracket in balanced_array
				if brackets_array[char_index+1] in balanced_array:
					# if a matching closing bracket is found in balanced_array,
					# remove it as it matches the opening bracket encountered
					balanced_array.remove(brackets_array[char_index+1])				
				else:
					# if no matching closing bracket is found in balanced_array
					# add the encountered opening bracket in our string into balanced_array
					balanced_array.append(char)

			# encountered character in the string is a closing bracket
			# all closing brackets are on odd positions
			else:
				# check to see if there is a matching opening bracket in the balanced array
				if brackets_array[char_index-1] in balanced_array:
					# if a matching opening bracket is found in balanced_array
					# remove it as it matches with the closing bracket encountered
					balanced_array.remove(brackets_array[char_index-1])
				else:
					# if no matching opening bracket is found in balanced_array
					# add the encountered closing bracket in our string into balanced_array
					balanced_array.append(char)

	# after looping through all characters in the string
	# if the length of balanced_array is greater than 0 (i.e if balanced_array is not empty)
	# return False as there is an unmatched bracket
	if len(balanced_array) > 0:
		return "False"

	# else return true as all brackets "cancelled" each other out and thus are balanced
	else:
		return "True"
	
def main():

	# try statement
	try:

		print "BALANCED BRACKET CHECK REPORT:"
		print "\n"

		string_input = raw_input("Enter a string with parenthesis: ")
		print "\n"

		print check_brackets(string_input, brackets_array)

	# Handle exceptions
	except Exception:
		print "An error has occured"

if __name__ == "__main__":

	try:
		sys.exit(main())

	except Exception:
		print "An error has occured"
