# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Fibonacci Series
# Project: python-escapade
# Package: classic-cs-programming-problems
#
# In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence, and characterized 
# by the fact that every number after the first two is the sum of the two preceding ones: 
#
# By definition, the first two numbers in the Fibonacci sequence are either 1 and 1, or 0 and 1, depending on the chosen starting point of the sequence, and each subsequent number is the sum of the previous two.
#
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
#
#    Fn = Fn − 1 + Fn − 2 ,
# with seed values
#	 F1 = 1, F2 = 1
# or
#
#    F0 = 0 , F1 = 1.
#
#============================================================================================================================================

import sys
	
def main(n):
	n= int(n)

	fibonacci_series = [0,1]

	for i in range(1,n-1):
		next_fibonacci_no = fibonacci_series[(len(fibonacci_series)-1)]+fibonacci_series[(len(fibonacci_series)-2)]
		fibonacci_series.append(next_fibonacci_no)

	print fibonacci_series

if __name__ == "__main__":
	try:
		sys.exit(main(sys.argv[1]))

	except Exception:
		print "An error has occured"
		print "To run this program, the number of Fibonacci numbers to be generated should be passed as a parameter"
		print "For instance, python fibonacci.py 5"
