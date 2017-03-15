# -*- coding: utf-8 -*-

#============================================================================================================================================
#
# Author: Kelvin Wahome
# Title: Fibonacci Series
# Project: python-escapade
# Package: turtle
#
# A simple program that draws a circle from squares
#
#============================================================================================================================================


import turtle

def draw_square(square_turtle):
	for i in range(1,5):
		square_turtle.forward(100)
		square_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(20)

	turn_angle = 3
	number_of_loops = 360/turn_angle+1

	for i in range(1,number_of_loops):
		draw_square(brad)
		brad.right(turn_angle)

	window.exitonclick()

draw_art()