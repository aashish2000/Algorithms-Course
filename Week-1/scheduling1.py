import operator

f=open("jobs.txt","r")
maxweight=0
count=0
no=0
jobs=[]
for line in f:
    line=line.rstrip("\n")
    if(count==0):
        no=int(line)
    else:
        lw,hw=map(int,line.split())
        jobs.append([lw,hw,lw-hw])
    count+=1

jobs=sorted(jobs,key=operator.itemgetter(2,0))
jobs = jobs[-1::-1]
sumTime = 0
sumLength = 0 
for job in jobs:
    sumLength += job[1]
    sumTime += job[0] * sumLength
print(sumTime)
