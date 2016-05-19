# usr/bin/python -tt
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:55:48 2016

@author: mohdkhan
"""
import os
import time
from email.parser import Parser
from os.path import isfile, join
from nltk.stem.snowball import *
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

class EmailParesr:
    
    def __init__(self):
        print "begin"
        
    
    
    def prepareData(self,path):
        rawemail_list=os.listdir(path)
        email_list = self.parseEmail(path,rawemail_list)
        #print "email list \n"
        #print email_list
        
    def GetMailParts(self,message):
        Subject = ""
        Skip = False
        if(Skip == False):
            Subject = Subject + str(message['subject'])
        return Subject
    
    '''    
    This function is respnosible for the all bag of words related operations 
    Input - unique subject list
    return bag of words
    '''
    def refactoring(self,emailList):
        minWordLength = 4
        lower_list = []
        bagOfWords = []
        
        stopWords = stopwords.words('english')
        stemmer = SnowballStemmer("english")
        for i in range(len(emailList)):
            text = (emailList[i]).lower().strip()
            text = ' '.join([word for word in text.split() if word not in stopWords])
            lower_list.append(text)

        #print lower_list
        lower_list = [stemmer.stem(word) for sentence in lower_list for word in sentence.split(" ")]
        
        #print lower_list
        bagOfWords = list(set(lower_list))
        print "Bag of words"
        return bagOfWords
        
    def skRefactor(self,emaillist):
        vectorizer = CountVectorizer(stop_words=stopwords.words('english'))
        bagOfWords = vectorizer.fit(emaillist)
        bagOfWords = vectorizer.transform(emaillist)
        print bagOfWords
        
    '''
    Input - Mail folder path    
    Return - 4 items
            unique subject list
            subject map , subject as key and value  Listof mail name
            onlyFiles list of mail name
    '''
    def parseEmail(self,path,raw_emails):
        onlyFiles = [] # list of all mails
        subject_list = [] #Unique subject list for the bag of words
        subject_map = {}  # map to grp same type of mail
        onlyFiles = [f for f in raw_emails if isfile(join(path, f))]
        
        print onlyFiles[20]
        for f in onlyFiles:        
            filePath = os.path.join(path, f)
        
            message = Parser().parse(open(filePath, 'r'), False)
            Subject=self.GetMailParts(message)
            
            if(subject_map.has_key(Subject)):
                subject_map[Subject].append(f)
            else:
                subject_map[Subject] = [f]
                
            subject_list.append(Subject)
            
        # Removing duplicate mails from the list and 
        subject_list = list(set(subject_list))
        
        #for key in subject_map.keys():
            #print key, subject_map[key]
            
            
        ''' creating bag of words from uniques subjects '''
        bagOfWords = self.refactoring(subject_list)
        #self.skRefactor(subject_list)
        #for i in range(len(subject_list)):
         #   print subject_list[i]
          #  print i
        print bagOfWords    
        return (subject_list ,subject_map ,onlyFiles ,bagOfWords)
        
        
    def decodingSubject(self,Subject):
        return Subject.decode('latin-1')
        
        
    

print "check"       
emailparse = EmailParesr()
#nltk.download()
start = time.asctime( time.localtime(time.time()) )

emailparse.prepareData(".//emailSample.obj")

end = time.asctime( time.localtime(time.time()) )
print start
print end