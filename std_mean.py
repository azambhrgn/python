# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 19:32:24 2016

@author: Azam
"""

import numpy as np
import scipy as sp


x=np.array([65,66,67,67,68,69,70,72])
#y=np.array([80,90,78,79,85])
y=np.array([67,68,65,68,72,72,69,71])
x_mean=sp.mean(x)
x_std=sp.std(x)

xy_cov=sp.cov(x,y)[0][1]

xy_pearson=sp.corrcoef(x,y)[0][1]

print "The mean is ",x_mean
print "The standard deviation is ",x_std
print "The cov is ",xy_cov
print "The correlation coefficient is ",xy_pearson
