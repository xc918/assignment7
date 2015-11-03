#Author: Xing Cui
#NetID: xc918
#Data: 11/02/2015

import numpy as np

def finding_nearest_point():
	"""The program should print out The 1D array containing 10 values, 
		each value is the number from 10*3 that closest to 0.5 from the corresponding row of the original array.
	"""
	array = np.random.rand(30).reshape(10,3)
	fixed_point = 0.5
	idx = np.abs(array - fixed_point).argsort()[:,0:1]	#get the absolute value of subtraction result and use the first colomn of argsort() as the index result.
	result_array = array[range(len(array)),idx.T]
	return result_array