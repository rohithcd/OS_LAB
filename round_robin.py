import pandas as pd
from operator import itemgetter

mylist=[]
newli=[]

tq=int(input("Enter the time quantum :"))
n=int(input("Enter the total number of processes : "))

for i in range(n):
    x=int(input("Enter the process number:"))
    y=int(input("Enter the arrivaltime:"))
    z=int(input("Enter the bursttime:"))
    mylist.append({'process':x,'arrivaltime':y,'bursttime':z})
    newli.append({'process':x,'arrivaltime':y,'bursttime':z})

mylist=sorted(mylist,key=itemgetter('arrivaltime'))
li=mylist

readyq=[]
x=0

total_BT=sum(item['bursttime'] for item in mylist )
readyq.append(mylist[0])

while x<total_BT:
    
    a=readyq.pop(0)
    bt=a['bursttime']
    bt=bt-tq
    a['bursttime']=bt
    if bt>0:
        
        x=x+tq
        for i in li:
            if (x-tq) <i['arrivaltime'] and (x)>=i['arrivaltime']:
                readyq.append(i)
                
        readyq.append(a)
        
        
    else:
        x=x+bt+tq
        for i in li:
            if (x-tq-bt)<i['arrivaltime'] and x<=i['arrivaltime']:
                readyq.append(i)
        
        ct=x
        for i in newli:
            if i['process']==a['process']:
                i['cmptime']=ct
                i['tatime']=i['cmptime']-i['arrivaltime']
                i['waitingtime']=i['tatime']-i['bursttime']

# newli=pd.DataFrame(newli)
# print(newli)

# total_waiting_time = newli['waitingtime'].sum()  
# avg_waiting_time = total_waiting_time/n
# print(f"Average Waiting Time :{avg_waiting_time}")

# total_turnaround_time = newli['tatime'].sum()  
# avg_turnaround_time = total_turnaround_time/n
# print(f"Average TurnAround Time :{avg_turnaround_time}")

print(newli)

total_waiting_time = sum(item['waitingtime'] for item in mylist)
avg_waiting_time = total_waiting_time/n
print(f"Average Waiting Time :{avg_waiting_time}")

total_turnaround_time = sum(item['turnaroundtime'] for item in mylist)  
avg_turnaround_time = total_turnaround_time/n
print(f"Average TurnAround Time :{avg_turnaround_time}")