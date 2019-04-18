import heapq
import math

f=open("edges.txt","r")
maxweight=0
count=0
for line in f:
    line=line.rstrip("\n")
    if(count==0):
        totv,tote=map(int,line.split())
        adjmat=[]
        for i in range(totv):
            adjmat.append([0]*totv)
    else:
        #print(adjmat)
        vi,vo,val=map(int,line.split())
        #adjmat[0][count-1]=val
        #print(vi,vo,val)
        if(val>maxweight):
            maxweight=val
        adjmat[vi-1][vo-1]=val
        adjmat[vo-1][vi-1]=val
    count+=1
    #print("count",count)
#print(adjmat,"max")
varr=[float("inf")]*totv
varr[0]=0

ve=[0]*totv
#print(varr,"varr")

flag=0
while(flag==0):
    ind=varr.index(min(varr))
    #print("ind",varr[ind])
    if(varr[ind]==maxweight+1):
        break
    else:
        for i in range(totv):
            if(adjmat[ind][i]!=0 and varr[i]>adjmat[ind][i] and varr[i]!=maxweight+1):
                varr[i]=adjmat[ind][i]
                ve[i]=ind
        varr[ind]=maxweight+1
    #print("newvarr",varr)
totweight=0

for i in range(totv):
    totweight+=adjmat[i][ve[i]]
#print("varr",varr)
print(totweight)
            


