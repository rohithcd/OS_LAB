import pandas as pd
from operator import itemgetter

mylist=[] #initialize list

n=int(input("Enter the total number of processes : ")) #Taking inputs
for i in range(n):
    x=int(input("Enter the process number:"))
    y=int(input("Enter the arrivaltime:"))
    z=int(input("Enter the bursttime:"))
    mylist.append({'process':x,'arrivaltime':y,'bursttime':z})

mylist=sorted(mylist, key=itemgetter('arrivaltime')) #sorting the list according to arrival time

burst_time=0 #initialize burst time
completion_time=0
for i in range(len(mylist)):#calculating completion time
    burst_time=mylist[i]['bursttime']
    completion_time=completion_time+burst_time
    if i>0 and mylist[i-1]['completiontime']>mylist[i]['arrivaltime']:
            mylist[i]['completiontime']=completion_time
    else:
        mylist[i]['completiontime']=mylist[i]['bursttime']+mylist[i]['arrivaltime']

waiting_time=0
for i in range(len(mylist)):#calculating waiting time
    if mylist[i]['arrivaltime']==0:
        mylist[i]['waitingtime']=0
        
    else:
        if i>0 and mylist[i-1]['completiontime']<mylist[i]['arrivaltime']:
            mylist[i]['waitingtime']=0
        else:
            waiting_time=mylist[i-1]['completiontime']-mylist[i]['arrivaltime']
            mylist[i]['waitingtime']=waiting_time
    mylist[i]['Turn-AroundTime']=mylist[i]['completiontime']-mylist[i]['arrivaltime']
  
mylist=pd.DataFrame(mylist)#converting list to dataframe
print(mylist)

total_waiting_time = mylist['waitingtime'].sum()  #calculating total waiting time
avg_waiting_time = total_waiting_time/n
print(f"Average Waiting Time : {avg_waiting_time}")

total_turnaround_time = mylist['Turn-AroundTime'].sum()  
avg_turnaround_time = total_turnaround_time/n
print(f"Average Turn Around Time : {avg_turnaround_time}")