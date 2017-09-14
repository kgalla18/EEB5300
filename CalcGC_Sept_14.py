#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:13:15 2017

@author: kaitlingallagher
"""

#opens file and stores it in the variable fh
fh = open("/Users/kaitlingallagher/Documents/EEB5300/demo.fasta", "r")
#store lines from fh into list called lines
lines = fh.readlines()

#calculating # of genes:
#this will let you tally number of genes
NumGenes=0
for l in lines:
    ##l refers to the element in the list, what is in the bracket refers to the first letter/symbol of that element
    if l[0]==">":
        #add a count to NumGenes to count # of genes
        NumGenes=NumGenes+1
        
#figuring out GC content
countA=0
countG=0
countC=0
countT=0
nuc=0
for l in lines:
    if l[0]!=">":
        for n in l:
            if n=="A":
                countA=countA+1
                nuc=nuc+1
            if n=="G":
                countG=countG+1
                nuc=nuc+1
            if n=="T":
                countT=countT+1
                nuc=nuc+1
            if n=="C":
                countC=countC+1
                nuc=nuc+1

print (countA)
print (countC)
print (countG)
print (countT)
print (nuc)
                
print (countA+countC+countG+countT)
        
GC=(countC+countG)/float(nuc)
print ("GC content is:", GC)
    