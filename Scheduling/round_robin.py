from operator import itemgetter


def takeInput():
    mylist = []
    num = int(input("Enter number of processes: "))
    qt = int(input("Enter quantum time: "))

    for i in range(num):
        process_num = int(input("Process number: "))
        arrival_time = int(input("Arrival time: "))
        burst_time = int(input("Burst time: "))

        mylist.append({'process_num': process_num, 'arrival_time': arrival_time,
                      'burst_time': burst_time, 'completion_time': 0, 'tat': 0, 'wt': 0})

    return mylist, qt


def sort_At(mylist):
    mylist = sorted(mylist, key=itemgetter('arrival_time'))

    return mylist


def sort_Bt(mylist):
    mylist = sorted(mylist, key=itemgetter('burst_time'))

    return mylist


def createReadyq(mylist, readyq, pno, qc_time):  # qc_time-quantum complete time
    # The remove() method removes the first matching element (which is passed as an argument) from the list.
    print("mylist_function")
    displayTable(mylist)
    for i in mylist:
        if i in readyq:
            mylist.remove(i)
    for i in range(len(mylist)):
        if mylist[i]['arrival_time'] <= qc_time and mylist[i]['process_num'] != pno:
            readyq.append(mylist[i])
    print("function readyq")
    displayTable(readyq)
    return readyq


def insertCompletionTime(mylist, qt):
    li = []
    readyq = []
    count = 0
    total_BT = sum(item['burst_time'] for item in mylist)
    readyq .append(mylist[0])
    
    while count <= total_BT:
        process = readyq.pop(0)
        
        if process['burst_time'] >= qt:
            process['completion_time'] = process['completion_time']+qt
            count = count+qt
            process['burst_time'] = process['burst_time']-qt
            
            readyq = createReadyq(
                mylist, readyq, process['process_num'], process['completion_time'])
            
            print("count", count)
            readyq.append(process)
            
            print("readdyq")
            displayTable(readyq)
        else:
            process['completion_time'] = process['completion_time'] + \
                process['burst_time']
            count = count+process['burst_time']
            process['burst_time'] = 0
            mylist.remove(process)
            readyq = createReadyq(
                mylist, readyq, process['process_num'], process['completion_time'])
            li.append(process)
            print("readdyq e")
            displayTable(readyq)
            print("count", count)

    print("li")
    displayTable(li)
    return li


def insertTatWat(mylist):
    for i in range(len(mylist)):
        mylist[i]['tat'] = mylist[i]['completion_time'] - \
            mylist[i]['arrival_time']
        mylist[i]['wt'] = mylist[i]['tat'] - mylist[i]['burst_time']
    return mylist


def displayTable(mylist):
    # mylist = sort_At(mylist)
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
    process_list, qt = takeInput()
    process_list = sort_At(process_list)
    process_list = insertCompletionTime(process_list, qt)
    process_list = insertTatWat(process_list)
    displayTable(process_list)
    displayAvg(process_list)


main()
