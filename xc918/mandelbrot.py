#Author: Xing Cui
#NetID: xc918
#Data: 11/02/2015



import numpy as np
import matplotlib.pyplot as plt

class mandelbrot(object):
    """This class is to create the classic Mandelbrot fractal using the Mandelbrot iteration
    """
    def __init__(self,x,y):
        self.N_max = 50             #define given information
        self.some_threshold = 50
        self.x = x
        self.y = y
        self.compute = self.mandelbrot_compute1()   #call the function mandelbrot_compute1
        
    def mandelbrot_compute1(self):
        #Using given fomulars to form 2D boolean mask by indicating all points in the set.
        c = self.x + 1j*self.y
        z = c
        for v in range(self.N_max):
            z = z**2 + c
            
        if abs(z) < self.some_threshold:
            return True
        else:
            return False
        
def mandelbrot_compute2(xmin,xmax,ymin,ymax,step):
    np.seterr(over = 'ignore', invalid = 'ignore')
    #get the range for x and y
    X = np.linspace(xmin,xmax,step)
    Y = np.linspace(ymin,ymax,step)
    #building up a meshgrid to put all point in
    mask = np.zeros((len(X),len(Y)))
    #giving each spot on meshgrid a true or false value
    for i in range(len(X)):
        for j in range(len(Y)):
            mask[i,j] = mandelbrot(X[i],Y[j]).compute
    return mask