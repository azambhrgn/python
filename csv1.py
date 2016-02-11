# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:19:28 2016

@author: Azam
"""

import csv
import random
import numpy as num
import matplotlib.pyplot as plt
import math

def loadData():
    f=open("kmean.csv","wb")
    l=[]
    wr=csv.writer(f)
    for i in range(9):
        if(i<=3):
            l.append([random.randint(1,10)])
        elif(i<=6):
            l.append([random.randint(20,30)])
        else:
            l.append([random.randint(40,50)])
    wr.writerow(l)
    f.close()

def readData():
    f=open("kmean.csv","rb")
    rdr=csv.reader(f)
    data=rdr
    f.close()
    return data
    
def euclideanDistance(a,b):
    dist=pow(a-b,2)
    return math.sqrt(dist)
    

def prepareData(data, centr):
    distnc=[]
    for x in range(len(data)-1):
        lst=[]
        for y in range(len(centr)-1):
            #lst.append(data[x])
            k=euclideanDistance(data[x],centr[y])
            lst.append(k)
        lst.append(num.argmin(lst))
        lst=data[x]+lst
        distnc.append(lst)
        
    print distnc
        
        
#loadData() 
      
data=readData()
k=3
print(data)
#centr=random.sample(data,k)

#for x in range(k-1):
    #centr[x]=float(centr[x])

#prepareData(data,centr)



plt.plot(data,'ro')
plt.xlim(0,12)
plt.ylim(0,55)
plt.show()
