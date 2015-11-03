#Author: Xing Cui
#NetID: xc918
#Data: 11/02/2015

import unittest
from unittest import TestCase
import numpy as np 
from mandelbrot import *

class Test_assignment7(TestCase):
	"""Test for assignment7"""
	def setUp(self):
		pass

	def test_init(self):
		x = -2
		y = -1
		m = mandelbrot(x,y)

		self.assertTrue(m.x == x)
		self.assertTrue(m.y == y)
		self.assertTrue(m.N_max == m.some_threshold)
		self.assertTrue(m.compute == False)

		
	def test_compute1(self):
		self.assertTrue(mandelbrot(0,0).compute)

	def test_compute2(self):
		np.seterr(over = 'ignore', invalid = 'ignore')
		X = np.linspace(-2,1,200)
		Y = np.linspace(-1.5,1.5,200)
		mask = np.zeros((len(X),len(Y)))
		for i in range(len(X)):
			for j in range(len(Y)):
				mask[i,j] = mandelbrot(X[i],Y[j]).compute
		self.assertTrue(np.array_equal(mandelbrot_compute2(-2,1,-1.5,1.5,200),mask))

if __name__ == '__main__':
    unittest.main()
