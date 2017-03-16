# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Interpolation Search Algorithm
# Project: python-escapade
# Package: fun-with-problems
#
#
# Suppose we could access yesterday's stock prices as a list, where:
#
#     The values are the price in dollars of Apple stock.
#     A higher index indicates a later time.
#
# So if the stock cost $500 at 10:30am and $550 at 11:00am, then:
#
# stock_prices_yesterday[60] = 500
#
# Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 
# 1 Apple stock yesterday. 
#
#============================================================================================================================================

import sys

def max_profit(stocks):

	# If the array is empty, we cannot make a profit.
    if len(stocks) == 0:
        return 0

    # Otherwise, keep track of the best possible profit and the lowest value
    # seen so far.
    profit = 0
    lowest = stocks[0]
    lowest_index = 0
    highest_index = 0

    # Iterate across the array, updating our answer as we go according to the
    # above pseudocode.
    for i in range(1, len(stocks)):
        # Update the minimum value to be the lower of the existing minimum and
        # the new minimum.
        lowest = min(lowest, stocks[i])

        # Take the index of the lowest stock value
        # Check to see if there is another equivalent earlier lower value so as to keep the earliest value 
        if lowest == stocks[i] and stocks[i] not in stocks[i:]:
        	lowest_index = i

        # Update the maximum profit to be the larger of the old profit and the
        # profit made by buying at the lowest value and selling at the current
        # price.
        profit = max(profit, stocks[i] - lowest)

        # Take the index of the highest stock value
        # Check to see if there is another equivalent later value so as to keep the earliest value
        if profit == (stocks[i] - lowest) and stocks[i] not in stocks[:i]:
        	highest_index = i

	results = {0: lowest_index, 1: highest_index, 2: profit}

    return results


def main():

	apple_stock = []

	print "Apple's stocks yesterday"
	print "------------------------"

	number = input("Enter the count of yesterday's Apple stock prices at different times (e.g. 10) ")
	print "\n"

	for i in range (1,number+1):
		apple_stock_value = input("Please enter the value of Apple's stock at time "+str(i)+" yesterday ")
		apple_stock.append(apple_stock_value)

	print "\n"
	print "Yesterday's Apple stock prices: "
	print apple_stock
	print "\n"

	response = max_profit(apple_stock)

	print "Maximum profit that you could have made:"
	print "\n"

	print " |-> Buy at time " + str(response.items()[0][1]) + " when the stock was worth $" + str(apple_stock[response.items()[0][1]])
	print " |-> Sell at time " + str(response.items()[1][1]) + " when the stock was worth $" + str(apple_stock[response.items()[1][1]])
	print " |-> Profit made : $" + str(response.items()[2][1])
	print "\n"

if __name__ == "__main__":
	
	# try:
	sys.exit(main())

	# except Exception:
	# 	print "An error has occured"
