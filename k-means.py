import numpy as np 
import pandas as pd
import random
import math
data = pd.read_excel('Course Evaluation .xlsx' ,usecols = ['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20'])
data.drop
data.values

students = []
for i in range(0,len(data)):
    students.append([int(data.values[i,j])for j in range (0,data.columns.size)])

print("Enter K: ")
k = input()
k=int(k)

def euclidean_distance(x1, x2):
    dis=0
    for i in range (data.columns.size):
       dis = dis + ((x1[i]-x2[i])**2)
    return math.sqrt(dis)



#----------------------------------First itteration--------------------------------------------

intialCentroidIndex=[]
intialCentroidIndex=(random.sample(range(len(data)), k))
intialCentroid=[]
x=0
while (True):    
    same=[]
    for i in range(k):
        if(x==0):
            intialCentroid.append(students[intialCentroidIndex[i]])
        
    for i in range(0,k):
        for j in range(i+1,k):
            if(intialCentroid[i]==intialCentroid[j]):
                if not(j in same):same.append(j)
    if (len(same)==0):break
    else:
        for a in range (len(same)):
            rand=random.sample(range(len(data)), 1)
            intialCentroid[same[a]]=(students[rand[0]])
            intialCentroidIndex[same[a]]=(rand[0])
            x+=1

similar=[]
for i in range(len(students)):
    dis=[]
    for j in range(k):
       dis.append(euclidean_distance( students[i] , students[intialCentroidIndex[j]]))       
    minDis= min(dis)
    similar.append(intialCentroidIndex[dis.index(minDis)])

#--------------------------------------- ******** -----------------------------------------
xx=0
N=0
prevMeans=[]
prevMeanss=[]
for s in range(len(similar)):
    prevMeans.append(students[similar[s]])   


means=[]
mean=[]
for j in range( len(intialCentroidIndex)):
    cluster=[]
    mean=[]
    
    for i in range (len(similar)):
        if (similar[i]== intialCentroidIndex[j]):
            cluster.append(students[i])
    for y in range(data.columns.size):
        Sum=0
        n=0
        for x in range(len(cluster)): 
             Sum+=cluster[x][y]
        if (len(cluster)>0):
            mean.append(Sum/len(cluster))   
        else:
            means.append(students[intialCentroidIndex[j]])
            n=1
            break
    if(n==0): means.append(mean)

prevMeanss=means
          
        
N=0

while (True):
    if not(N==0):means=[]    
    mean=[]

                        
    if (N>0):
        for i in range (k):
            cluster=[]
            for j in range(len(similar)):
                if (similar[j]==prevMeanss[i]):
                    cluster.append(students[j])
            for y in range(data.columns.size):
                Sum=0
                n=0
                for x in range(len(cluster)): 
                     Sum+=cluster[x][y]
                mean.append(Sum/len(cluster))   
            means.append(mean)
            mean=[] 



    mean=[]    
    similar=[]
    for i in range(len(students)):
        dis=[]
        for j in range(k):
           dis.append(euclidean_distance( students[i] , means[j]))
        minDis= min(dis)
        similar.append(means[dis.index(minDis)])
        
    if (prevMeans==similar):break
    else:
        prevMeans=[]
        prevMeanss=means
        prevMeans=similar

    N+=1


sizes=[]
for i in range (k):
    ctr=0
    print ("cluster (" , i+1 ,")")
    print(means[i])
    print("Data")
    for j in range(len(similar)):
        if (similar[j]==means[i]):
            print("student (" , j ,') ', students[j])
            ctr+=1
    sizes.append(ctr)

ctr2=0    
print("outlier data:")
minSize = min(sizes)
for i in range (k):
    if (minSize==sizes[i]):
        ctr2+=1
        
for i in range (k):
    if (minSize==sizes[i] and ctr2<len(sizes)):
        print("cluster (",i+1,")")
    
    
        
    
