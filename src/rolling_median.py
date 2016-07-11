
# coding: utf-8

# In[6]:

#import numpy as np
import os.path
import json
import collections
import datetime
from statistics import median 

fpath = os.path.join("venmo_input", "venmo-trans.txt")
opath = os.path.join("venmo_output", "output.txt")
#open(fpath).readlines()[:4]

json_data=open(fpath).readline()
data = json.loads(json_data)

maxtimestamp=datetime.datetime(1, 1, 1, 1, 1, 1)
datehv1=data['created_time'].replace('T', ' ')
datahv2=datehv1.replace('Z', '')
transdatetime=datetime.datetime.strptime(datahv2, "%Y-%m-%d %H:%M:%S")

TranLast60 =[]
outfile=open(opath,'w')
outfile.close()

meddegreetime=[]
outfile=open(opath,'w')
maxtimestamp=datetime.datetime(1, 1, 1, 1, 1, 1)
for line in open(fpath):
    data = json.loads(line)
    datehv1=data['created_time'].replace('T', ' ')
    datahv2=datehv1.replace('Z', '')
    transdatetime=datetime.datetime.strptime(datahv2, "%Y-%m-%d %H:%M:%S")
    if data['actor']!='' and data['target']!='' and data['created_time']!='':
        TranLast60.append([transdatetime,data['actor'],data['target']])
        if transdatetime>maxtimestamp:
            maxtimestamp=transdatetime
    else:
        print('one transaction at ',data['created_time'],' ignored due to curropted data')

    # This part filter the transactions
    FilteredTranLast60=[]
    for recordind, recordvalue in enumerate(TranLast60):
           if not (TranLast60[recordind][0]-maxtimestamp)> datetime.timedelta(seconds=60) and not (maxtimestamp-TranLast60[recordind][0])> datetime.timedelta(seconds=60):
                FilteredTranLast60.append(TranLast60[recordind])
    TranLast60=FilteredTranLast60
    
    
    #for recordind, recordvalue in enumerate(TranLast60):
    #    if (TranLast60[recordind][0]-maxtimestamp)> datetime.timedelta(seconds=60) or (maxtimestamp-TranLast60[recordind][0])> datetime.timedelta(seconds=60):
    #        TranLast60.pop(recordind)
    
    graph=collections.defaultdict(list)
    for recordind, recordvalue in enumerate(TranLast60):
        graph[TranLast60[recordind][1]].append(TranLast60[recordind][2])
        graph[TranLast60[recordind][2]].append(TranLast60[recordind][1])
    
    degree={}
    for key in graph:
        if len(list(set(graph[key])))>0:
            degree[key]=len(list(set(graph[key])))
    currentmeddegree=median(sorted(degree.values()))  
    outfile.write(str(currentmeddegree)+'\n')
    meddegreetime.append(currentmeddegree)
outfile.close()    


# In[ ]:



