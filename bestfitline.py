# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 22:27:08 2016

Finding and plotting the best fit line

@author: Azam
"""

import scipy as sp
import numpy as np

x=np.array([89,66,78,111,44,77,80,66,109,76])
y=np.array([7,5.4,6.6,7.4,4.8,6.4,7,5.6,7.3,6.4])

x_mean=sp.mean(x)
y_mean=sp.mean(y)

std_x=sp.std(x)
std_y=sp.std(y)

#Correlation coefficient
r=sp.corrcoef(x,y)[0][1]

m_y=r*(std_y/std_x)
m_x=r*(std_x/std_y)

b_y=y_mean-m_y*x_mean
b_x=x_mean-m_x*y_mean

print "m for the y is ", m_y
print "b for the y is ", b_y

#u=70 #raw_input("Enter the value of y for prdiction of X ")

#v=m_x*u+b_x

#print "X = ",v





