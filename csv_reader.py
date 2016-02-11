# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 00:05:25 2016
Reading from CSV file
@author: Azam
"""

import csv
import random
import math
import operator

def loadDataset(filename,split,trainingset=[],testSet=[]):
    f=open(filename,'rb')
    reader = csv.reader(f)
    dataset = list(reader)

    for x in range(len(dataset)-1):
        for y in range(4):
            dataset[x][y]=float(dataset[x][y])
        if random.random() < split:
                trainingset.append(dataset[x])
        else:
                testSet.append(dataset[x])
              

def euclideanDistance(inst1, inst2, length):
    distance=0
    for x in range(length):
        distance += pow(inst1[x] - inst2[x], 2)
    return math.sqrt(distance)


def getNeighbors(trainingset, data, k):
    distances=[]
    length= len(data)-1
    for x in range(len(trainingset)):
        dist=euclideanDistance(trainingset[x], data, length)
        distances.append((trainingset[x],dist))
    distances.sort(key=operator.itemgetter(1))
    #print distances
    neighbor=[]
    for i in range(k):
        neighbor.append(distances[i][0])
    return neighbor
    

def getResponse(neighbors):
    classVotes={}
    for x in range(len(neighbors)):
        response=neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else :
            classVotes[response]=1
    
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
    
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	print 'Checking'
	per= (correct/float(len(testSet))) * 100.0
	print per
	return per
    
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	split = 0.67
	loadDataset('iris.data', split, trainingSet, testSet)
	print 'Train set: ' + repr(len(trainingSet))
	print 'Test set: ' + repr(len(testSet))
	# generate predictions
	predictions=[]
	k = 3
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors)
		predictions.append(result)
		print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
	#print testSet
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: ' + repr(accuracy) + '%')
	
main()
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    