from operator import itemgetter


def takeInput():
    mylist = []
    num = int(input("Enter number of processes: "))

    for i in range(num):
        process_num = int(input("Process number: "))
        arrival_time = int(input("Arrival time: "))
        burst_time = int(input("Burst time: "))

        mylist.append({'process_num': process_num, 'arrival_time': arrival_time,
                      'burst_time': burst_time, 'completion_time': 0, 'tat': 0, 'wt': 0})

    return mylist


def sort_At_Bt(mylist):
    mylist = sorted(mylist, key=itemgetter('arrival_time', 'burst_time'))

    return mylist


def sort_Bt(mylist):
    mylist = sorted(mylist, key=itemgetter('burst_time'))

    return mylist


def createReadyq(mylist, order_list, end):
    readyq = []
    # The remove() method removes the first matching element (which is passed as an argument) from the list.
    for i in mylist[:]:
        if i in order_list:
            mylist.remove(i)
    for i in range(len(mylist)):
        if mylist[i]['arrival_time'] <= end:
            readyq.append(mylist[i])
    readyq = sort_Bt(readyq)

    return readyq


def insertCompletionTime(mylist):
    li = []
    mylist[0]['completion_time'] = mylist[0]['arrival_time'] + \
        mylist[0]['burst_time']
    li.append(mylist[0])

    for i in range(1, len(mylist)):
        readyq = createReadyq(mylist, li, li[i-1]['completion_time'])
        li.append(readyq[0])
        if li[i]['arrival_time'] < li[i-1]['completion_time']:
            li[i]['completion_time'] = li[i -
                                          1]['completion_time'] + li[i]['burst_time']
        else:
            li[i]['completion_time'] = li[i]['arrival_time'] + li[i]['burst_time']
    return li


def insertTatWat(mylist):
    for i in range(len(mylist)):
        mylist[i]['tat'] = mylist[i]['completion_time'] - \
            mylist[i]['arrival_time']
        mylist[i]['wt'] = mylist[i]['tat'] - mylist[i]['burst_time']
    return mylist


def displayTable(mylist):
    mylist = sort_At_Bt(mylist)
    print("\nPN\tAT\tBT\tTAT\tWT\tCT")
    for dict in mylist:
        pn = dict.get('process_num')
        at = dict.get('arrival_time')
        bt = dict.get('burst_time')
        tat = dict.get('tat')
        wt = dict.get('wt')
        ct = dict.get('completion_time')
        print(f"{pn}\t{at}\t{bt}\t{tat}\t{wt}\t{ct}")


def displayAvg(mylist):
    n = len(mylist)
    total_waiting_time = sum(item['wt'] for item in mylist)
    avg_waiting_time = total_waiting_time/n
    print(f"\nAverage Waiting Time :{avg_waiting_time}")

    total_turnaround_time = sum(item['tat'] for item in mylist)
    avg_turnaround_time = total_turnaround_time/n
    print(f"\nAverage TurnAround Time :{avg_turnaround_time}")


def main():
    process_list = takeInput()
    process_list = sort_At_Bt(process_list)
    process_list = insertCompletionTime(process_list)
    process_list = insertTatWat(process_list)
    displayTable(process_list)
    displayAvg(process_list)


main()
