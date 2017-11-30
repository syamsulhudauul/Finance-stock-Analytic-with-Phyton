# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:52:46 2017

@author: Syamsul
"""

print("====Finance Analityc====")
print("created by uul")
import csv
import numpy as np

f3 = open('RESOURCE/UNTR.JK28112015.csv')
f2 = open('RESOURCE/SMGR.JK28112015.csv')
f1 = open('RESOURCE/TLKM.JK28112015.csv')

csvf_1 = csv.reader(f1)
csvf_2 = csv.reader(f2)
csvf_3 = csv.reader(f3)

s1 = []
s2 = []
s3 = []
#print(n)
for row in csvf_1:
    #print(row[2])
    s1.append(row)

for row in csvf_2:
    #print(row[2])
    s2.append(row)

for row in csvf_3:
    #print(row[2])
    s3.append(row)

n = len(s1)
#print(ndata)
f1.close


stock=[]
for i in range(1,n):
    if ((s1[i][5]!="null") & (s2[i][5]!="null") & (s3[i][5]!="null")):
        #print(s1[i][0]+"\t"+s1[i][5]+"\t"+s2[i][5]+"\t"+s3[i][5])
        stock.append([s1[i][0],float(s1[i][5]),float(s2[i][5]),float(s3[i][5])])
        #print(stock[i][0]+"\t"+stock[i][1]+"\t"+stock[i][2]+"\t"+stock[i][3])
        
ndata=len(stock)

""""
#output data process
for i in range(1,ndata):
    print(stock[i][0]+"\t",stock[i][1],"\t",stock[i][2],"\t",stock[i][3])
"""    
        
r=[]
for i in range(2,ndata):
    tmp1=(stock[i][1]-stock[i-1][1])/stock[i-1][1]
    tmp2=(stock[i][2]-stock[i-1][2])/stock[i-1][2]
    tmp3=(stock[i][3]-stock[i-1][3])/stock[i-1][3]
    r.append([tmp1,tmp2,tmp3]) 
    #print(stock[i][0]+"\t",tmp1,"\t",tmp2,"\t",tmp3)      
  
arr = np.array(r)
stds = np.std(arr,axis=0)

bobot1 = 0.33;
bobot2 = 0.33;
bobot3 = 0.34;

expectedReturn = []
for i in range(1,ndata-2):
    #print(r[i][1])
    expectedReturn.append(float(bobot1*float(r[i][0])+bobot2*float(r[i][1])+bobot3*float(r[i][2])))

#menghitung korelasi

kor = np.var(arr,axis=0)