import math
import operator

f=open("clustering1.txt","r")
maxweight=0
edge=[]
head=[]
size=[]
k=0
count=0
for line in f:
    line=line.rstrip("\n")
    if(count==0):
        totv=(int(line))
        k=totv
        for i in range(k):
            head.append(i)
            size.append(1)
    else:
        vi,vo,val=map(int,line.split())
        edge.append([vi-1,vo-1,val-1])
    count+=1

edge=sorted(edge,key=operator.itemgetter(2))
for i in range(len(edge)):
    if(k==4):
        break
    if(head[edge[i][0]]!=head[edge[i][1]]):
        size[max(size[edge[i][0]],size[edge[i][1]])]+=size[min(size[edge[i][0]],size[edge[i][1]])]
        size[min(size[edge[i][0]],size[edge[i][1]])]=0
        for j in range(totv):
            if(head[j]==head[min(size[edge[i][0]],size[edge[i][1]])]):
                head[j]=max(size[edge[i][0]],size[edge[i][1]])
    k-=1

print(edge[i][2])