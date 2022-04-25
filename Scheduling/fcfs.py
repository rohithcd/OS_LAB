from operator import itemgetter

def takeInput():
    mylist = []

    num_process = int(input("Enter the total number of processes : "))
    for i in range(num_process):
        process_num=int(input("Process Number:"))
        arrival_time=int(input("Arrival Time:"))
        burst_time=int(input("Burst Time:"))
        mylist.append({'process_num':process_num,'arrival_time':arrival_time,'burst_time':burst_time})
    return mylist

def sortList(mylist):
    mylist=sorted(mylist,key=itemgetter('arrival_time'))
    return mylist

def insertCompletionTime(mylist):
    mylist[0]['completion_time']=mylist[0]['arrival_time'] + mylist[0]['burst_time']
    for i in range(1,len(mylist)):
        if mylist[i]['arrival_time'] < mylist[i-1]['completion_time']:
            mylist[i]['completion_time']=mylist[i-1]['completion_time'] + mylist[i]['burst_time']
        else:
            mylist[i]['completion_time']=mylist[i]['arrival_time'] + mylist[i]['burst_time']
    return mylist

def insertTatWat(mylist):
    for i in range(len(mylist)):
        mylist[i]['tat'] = mylist[i]['completion_time'] - mylist[i]['arrival_time']
        mylist[i]['wt'] = mylist[i]['tat'] - mylist[i]['burst_time']
    return mylist

def display(mylist):
    print("\nPN\tAT\tBT\tTAT\tWT")
    for dict in mylist:
        pn=dict.get('process_num')
        at=dict.get('arrival_time')
        bt=dict.get('burst_time')
        tat=dict.get('tat')
        wt=dict.get('wt')
        print(f"{pn}\t{at}\t{bt}\t{tat}\t{wt}")
        
def displayAvg(mylist):
    n=len(mylist)
    total_waiting_time=sum(item['wt'] for item in mylist)
    avg_waiting_time=total_waiting_time/n
    print(f"\nAverage Waiting Time :{avg_waiting_time}")

    total_turnaround_time=sum(item['tat'] for item in mylist)
    avg_turnaround_time=total_turnaround_time/n
    print(f"\nAverage TurnAround Time :{avg_turnaround_time}")

def main():
    process_list = takeInput()
    process_list=sortList(process_list)
    process_list=insertCompletionTime(process_list)
    process_list=insertTatWat(process_list)
    display(process_list)
    displayAvg(process_list)
main()