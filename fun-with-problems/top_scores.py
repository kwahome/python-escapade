# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Ranking players' scores
# Project: python-escapade
# Package: fun-with-problems
#
#
# You created a game that is more popular than Angry Birds. 
#
# You rank players in the game from highest to lowest score. 
# So far you're using an algorithm that sorts in O(nlgn)O(n\lg{n})O(nlgn) time, but players are complaining that their rankings aren't updated 
# fast enough. You need a faster sorting algorithm.  
# 
# Write a function that takes:
#
#    a list of unsorted_scores
#    the highest_possible_score in the game
#
# and returns a sorted list of scores in less than O(n lg n) time.
# 
# We’re defining n as the number of unsorted_scores because we’re expecting the number of players to keep climbing.
# 
# And we'll treat highest_possible_score as a constant instead of factoring it into our big O time and space costs, because the highest 
# possible score isn’t going to change. Even if we do redesign the game a little, the scores will stay around the same order of magnitude. 
#
#============================================================================================================================================

import sys

HIGHEST_POSSIBLE_SCORE = 100

def scores_ranking(scores, highest_possible_score):

	# list of 0s at indices 0..highest_possible_score
	score_counts = [0] * (highest_possible_score+1)

	# populate score_counts
	for score in scores:
		score_counts[score] += 1

	# populate the final sorted list
	sorted_scores = []

	# for each item in score_counts
	for score, count in enumerate(score_counts):

		# for the number of times the item occurs
		for time in range(count):
			# add it to the sorted list
			sorted_scores.append(score)

	return sorted_scores

def main():

	player_scores = []
	proceed = False

	print "Angry Birds players' scores ranking"
	print "-----------------------------------"

	while proceed is False:
		number = input("Enter the number of player scores in to rank ")
		if number >= 1: proceed = True
		else: print "At least one player score is required"
		print "\n"

	for i in range (1,number+1):
		score = input("Please enter player "+str(i)+"'s score: ")
		player_scores.append(score)

	print "\n"
	print "Entered list of players' scores: "
	print player_scores
	print "\n"

	print "Ranked scored:"
	print "\n"
	print scores_ranking(player_scores, HIGHEST_POSSIBLE_SCORE)

	print "\n"

if __name__ == "__main__":
	
	# try:
	sys.exit(main())

	# except Exception:
	# 	print "An error has occured"
