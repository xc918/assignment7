#Author: Xing Cui
#NetID: xc918
#Data: 11/02/2015


import numpy as np

def initial_2d_arrays():
    #Creating a 2 dimension array, named two_d_array
    two_d_array = np.arange(1,16).reshape(3,5).T
    return two_d_array
    
#Q1a
def array_rows(new_array):
    """Generate a new array containing the 2nd and 4th rows.
    """
    new_array = initial_2d_arrays()
    return new_array[[1,3],:]
#Q1b
def array_colomns(new_array):
    """Generate a new array that contains the 2nd column.
    """
    new_array = initial_2d_arrays()
    return new_array[:,1]

#Q1c
def array_rectangular_section(new_array):
    """Generate a new array that contains all the elements in the rectangular section 
        between the coordinates [1,0] and [3,2]
    """
    new_array = initial_2d_arrays()
    return new_array[1:4,:]
    
#Q1d
def array_element_values(array):
    """Generate a new array that contains only elements with values that are between 3 and 11
    """
    new_array = initial_2d_arrays()
    array_segment = array[array>3]#getting elements greater than 3 as a segment
    array_btw_3_11 = array_segment[array_segment <11]#generating elements between 3 and 11.
    return array_btw_3_11

    
   


