#Author: Xing Cui
#NetID: xc918
#Data: 11/02/2015

import numpy as np 
import matplotlib.pyplot as plt 
from learning_2d_arrays import *
from array_division import *
from nearest_point import *
from mandelbrot import *



"""This is the main program for assignment7. """

try:
	#Q1
	print 'Question 1: \n'
	print 'Initial array: '
	new_array = initial_2d_arrays()
	print new_array
	#Q1a
	print 'Generate a new array containing the 2nd and 4th rows: \n'
	print array_rows(new_array)
	#Q1b
	print 'Generate a new array that contains the 2nd column: \n'
	print array_colomns(new_array)
	#Q1c
	print 'Generate a new array that contains all the elements in the rectangular section between the coordinates [1,0] and [3,2]'
	print array_rectangular_section(new_array)
	#Q1d
	print 'Generate a new array that contains only elements with values that are between 3 and 11:'
	print array_element_values(new_array)

	#Q2
	print 'Question 2: \n'
	print 'The answer of a 5*5 array divided each column element-wise by a 1*5 array is: \n'
	print array_division_computing()

	#Q3
	print 'Question 3: \n'
	print 'The 1D array containing 10 values, each value is the number from 10*3 that closest to 0.5 from the corresponding row.'
	print finding_nearest_point()

	#Q4
	print 'Question 4: \n'
	print 'Ploting...'
	mask = mandelbrot_compute2(-2, 1, -1.5, 1.5, 1000) 
	plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
	plt.gray()
	plt.savefig('mandelbrot.png')
	
	print 'Plot the graph and save it to \'mandelbrot.png\''



except KeyboardInterrupt:
	print 'Oops, interruption.'
except TypeError:
	print 'Oops, invalid type.'
except ValueError:
	print 'Oops, invalid value.'
except ZeroDivisionError:
	print 'Oops, CANNOT divided by zero.'
except OverflowError:
	print 'Oops, Math error, overflow.'









