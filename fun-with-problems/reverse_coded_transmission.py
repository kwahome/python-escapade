# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Reversing coded word transmissions
# Project: python-escapade
# Package: fun-with-problems
#
#
# You're working on a secret team solving coded transmissions.
#
# Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault. 
# The message has been mostly deciphered, but all the words are backwards! Your colleagues have handed off the last step to you. 
# 
# Write a function reverse_words() that takes a string message and reverses the order of the words in-place. 
#
#============================================================================================================================================

import sys
import operator

def reverse_words(message):

	message_array = message.split(" ")

	reversed_message = message_array[len(message_array)-1]

	for i in range(len(message_array[:len(message_array)-1]),0,-1):
		reversed_message =  " ".join([reversed_message, message_array[i-1]])

	return reversed_message.strip()

def main():

	proceed = False

	print "Scrambling to decipher a recent message"
	print "---------------------------------------"

	message = raw_input("Enter the coded string to reverse: ")

	print "\n"
	print "Coded message: "
	print message
	print "\n"

	print "Reversed message:"
	print "\n"
	print reverse_words(message)

	print "\n"

if __name__ == "__main__":
	
	# try:
	sys.exit(main())

	# except Exception:
	# 	print "An error has occured"
