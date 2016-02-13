# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:43:43 2016

@author: Azam
"""

import csv
import random
import numpy as num
import matplotlib.pyplot as plt
import math

def loadData(m):
    f=open("kmean.csv","wb")
    l=[]
    wr=csv.writer(f)
    for i in range(m):
        if(i<m/3):
            l.append(float(random.randint(1,10)))
        elif(i<(2*m/3)):
            l.append(float(random.randint(20,30)))
        else:
            l.append(float(random.randint(40,50)))
    wr.writerow(l)
    print l
    f.close()
    
def readData(data,centroid,k):
    f=open("kmean.csv","rb")
    rdr=csv.reader(f)
    for row in rdr:
        data=row
    
    for i in range(len(data)):
        data[i]=float(data[i])
    
    f.close()
    return data
  
def euclideanDistance(a,b):
    dist=pow(a-b,2)
    return math.sqrt(dist)
    

def prepareoprList(data,centorid):
    oprlist=[]
    for x in range(len(data)):
        rowlist=[]
        rowlist.append(data[x])
        temp=[]
        for y in range(len(centorid)):
            dist=euclideanDistance(data[x],centorid[y])
            temp.append(dist);
        rowlist.append(num.argmin(temp))
        #rowlist.append(temp)
        oprlist.append(rowlist)
    return oprlist

def redefineCentorid(oprlist,centroid):
    centr_new=[]
    for x in range(len(centroid)):
        temp=[]
        for y in range(len(oprlist)):
            o_c=oprlist[y][1]
            if(o_c == x):
                temp.append(oprlist[y][0])
               # print "list value ",oprlist[y][0]
        mean_x=num.mean(temp)
        centr_new.append(mean_x)    
    #print centr_new        
    return centr_new

def printlist(oprlist):
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    for x in range(len(oprlist)):
        print oprlist[x]
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def main():
    data=[]
    centroid=[]
    m=15
    k=5
    #print centroid['c1']
    loadData(m)
    data=readData(data,centroid,k)
    
    centroid=random.sample(data,k)
    oprlist=prepareoprList(data,centroid)
    print centroid
    
    printlist(oprlist)
    old_centroid=centroid
    centroid=redefineCentorid(oprlist,centroid)
    oprlist=prepareoprList(data,centroid)
    print "Centorid= ",centroid
    printlist(oprlist)
    while(old_centroid != centroid):
        centroid=redefineCentorid(oprlist,centroid)
        oprlist=prepareoprList(data,centroid)
        print "Centorid = ",centroid
        printlist(oprlist)       
        old_centroid=centroid    
            
     
    print "Centorid= ",centroid
    
    
    
main()