# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:28:46 2016

@author: Azam
"""
import random
import csv
import math

def loadData(file_name) :
    f=csv.reader(open(file_name,"rb"))
    data=list(f)
    
    for x in range(len(data)):
        data[x]= [float(y) for y in data[x]]
    
    return data
    

def splitData(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]
    

def seprateDataOnBasesOfClass(dataset) :
    seprate={}
    for i in range(len(dataset)):
        temp=dataset[i]
        if (temp[-1] not in seprate):
            seprate[temp[-1]] = []
        seprate[temp[-1]].append(temp)
    return seprate
    
        
def findMean(values) :
    mean_val=sum(values)/len(values)
    return mean_val   
   
    
def findStd(values) :
    mean_val=sum(values)/len(values)
    std_val=math.sqrt(sum([pow(x-mean_val,2) for x in values])/(len(values)-1))
    return std_val;
    
def classification(dataset) :
    classified = [(findMean(x),findStd(x)) for x in zip(*dataset)]
    del classified[-1]
    return classified;

def classificationOnBasesOfClass(dataset) :
    seprate= seprateDataOnBasesOfClass(dataset)
    finalclassified={}
    for classValue,values in seprate.iteritems():
        finalclassified[classValue]=classification(values)
    return finalclassified


def calculatePdf(x,mean,stdev) :
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
    
def findProbbaility(classified, test) :
    prob={}
    for classValue,values in classified.iteritems():
        prob[classValue]=1
        for i in range(len(values)):
            (mean,stddev)=values[i]
            temp=test[i]
            prob[classValue] *= calculatePdf(temp,mean,stddev)
    #print prob
    return prob
    
def predicttions(classified,test):
    prob=findProbbaility(classified,test)
    bestLabel, bestProb = None, -1
    for classValue,values in prob.iteritems():
        if bestLabel is None or values > bestProb:
            bestProb=values;
            bestLabel=classValue
    return bestLabel;
    
    
def getPrediction(classified,testdata):
    prediction=[]
    for i in range(len(testdata)):
        result=predicttions(classified,testdata[i])
        prediction.append(result)
    return prediction
    
def calculateAccuracy(testset, predictdata):
    correct=0;
    for i in range(len(testset)):
        if testset[i][-1] == predictdata[i]:
            correct += 1
    accuracy = (correct/float(len(testset))) * 100.0;
    print "Correct ", correct ,"Out of ",len(testset);
    return accuracy;
    
        


def main():
    
    file_name="pima-indians-diabetes.data";
    splitRatio = .7
    #load data
    data=loadData(file_name);
    #print data
    # Split data 
    trainingset,testset=splitData(data,splitRatio)
    #print trainingset
    #classified Data
    classified=classificationOnBasesOfClass(trainingset)
    #print classified 
    # Get Prediction
    predictdata= getPrediction(classified,testset)
    #print predictdata
    accuracy = calculateAccuracy (testset,predictdata)
    print "Accuracy ", accuracy    
    
    
main()
    
        