# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Merging Ranges
# Project: python-escapade
# Package: fun-with-problems
#
#
# Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
#
# To do this, you’ll need to know when any team is having a meeting. 
# In HiCal, a meeting is stored as tuples ↴ of integers (start_time, end_time). 
# These integers represent the number of 30-minute blocks past 9:00am.  
#
# For example: 
# 	(2, 3) # meeting from 10:00 – 10:30 am
# 	(6, 9) # meeting from 12:00 – 1:30 pm
#
# Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges. 
#
# For example, given: 
# [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#
# your function would return: 
# [(0, 1), (3, 8), (9, 12)]
#
# Do not assume the meetings are in order. The meeting times are coming from multiple teams.
#
#============================================================================================================================================

import sys
import operator

def merge_ranges(meetings_list):

	# sort by start times
	meetings_list = sorted(meetings_list)

	# initialize merged_meetings with the earliest meeting
	merged_meetings = [meetings_list[0]]

	for current_meeting_start, current_meeting_end in meetings_list[1:]:

		last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

		# if the current and last meetings overlap, use the latest end time
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

        # add the current meeting since it doesn't overlap
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))

	return merged_meetings

def main():

	meetings = []
	proceed = False

	print "Merging Meeting Ranges"
	print "----------------------"

	while proceed is False:
		number = input("Enter the number of meetings ")
		if number > 1: proceed = True
		else: print "Merging meeting ranges requires at least 2 meetings"
		print "\n"

	for i in range (1,number+1):
		start = input("Meeting "+str(i)+" starts at: ")
		end = input("Meeting "+str(i)+" ends at: ")
		meetings.append((start,end))

	print "\n"
	print "Meetings in the calender: "
	print meetings
	print "\n"

	print "Merged meetings calender:"
	print "\n"
	print merge_ranges(meetings)

	print "\n"

if __name__ == "__main__":
	
	# try:
	sys.exit(main())

	# except Exception:
	# 	print "An error has occured"
