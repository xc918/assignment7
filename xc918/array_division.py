#Author: Xing Cui
#NetID: xc918
#Data: 11/02/2015

import numpy as np

def array_division_computing():
	"""Calculating a 5*5 array divided each column element-wise by a 1*5 array
	"""
	a = np.arange(25).reshape(5, 5)
	b = np.array([1., 5, 10, 15, 20])
	division = np.divide(a,b)			#use np.divide() to culculate.
	return division



