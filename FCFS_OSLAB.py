import pandas as pd
from operator import itemgetter

mylist=[]

n=int(input("Enter the total number of processes : "))
for i in range(n):
    x=int(input("Enter the process number:"))
    y=int(input("Enter the arrivaltime:"))
    z=int(input("Enter the bursttime:"))
    mylist.append({'process':x,'arrivaltime':y,'bursttime':z})

mylist= sorted(mylist , key=itemgetter('arrivaltime'))

#completion time
mylist[0]['completiontime']=mylist[0]['arrivaltime']+mylist[0]['bursttime']

#Turnaround time
mylist[0]['turnaroundtime']=mylist[0]['completiontime']-mylist[0]['arrivaltime']

# waiting time
mylist[0]['waitingtime']=mylist[0]['turnaroundtime']-mylist[0]['bursttime']

queue=[]

# insert remaining elements into queue
queue=mylist[1:] # instead of 1 we can use a variable if first element

BURSTTIME=mylist[0]['completiontime']


flag=0
if queue[0]['arrivaltime']>BURSTTIME:
    BURSTTIME=queue[0]['bursttime']+queue[0]['arrivaltime']
    flag=1
    x+=BURSTTIME        
for i in queue:
    i['completiontime']=BURSTTIME if flag==1 else BURSTTIME+i['bursttime']
    i['turnaroundtime']=i['completiontime']-i['arrivaltime']
    i['waitingtime']=i['turnaroundtime']-i['bursttime']
    BURSTTIME=i['completiontime']
    x+=BURSTTIME
        
# mylist = pd.DataFrame(mylist)
# print(mylist)

# total_waiting_time = mylist['waitingtime'].sum()  
# avg_waiting_time = total_waiting_time/n
# print(f"Average Waiting Time :{avg_waiting_time}")

# total_turnaround_time = mylist['turnaroundtime'].sum()  
# avg_turnaround_time = total_turnaround_time/n
# print(f"Average TurnAround Time :{avg_turnaround_time}")


print(mylist)

total_waiting_time = sum(item['waitingtime'] for item in mylist)
avg_waiting_time = total_waiting_time/n
print(f"Average Waiting Time :{avg_waiting_time}")

total_turnaround_time = sum(item['turnaroundtime'] for item in mylist)  
avg_turnaround_time = total_turnaround_time/n
print(f"Average TurnAround Time :{avg_turnaround_time}")