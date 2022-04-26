def main():
    quantum = 2
    total_bt = 0
    total_wt = 0
    total_tt = 0
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        process = {}
        process['id'] = i+1
        process['burst_time'] = int(
            input("Enter burst time of process "+str(i+1)+": "))
        process['arrival_time'] = int(
            input("Enter arrival time of process "+str(i+1)+": "))
        process['remaining_time'] = process['burst_time']
        process['isExecuted'] = False
        processes.append(process)
        total_bt += process['burst_time']
    current_time = 0
    current_proc = 0
    ready_queue = []
    print()

    while current_time < total_bt:
        for i in range(n):
            if processes[i]['arrival_time'] <= current_time and not processes[i]['isExecuted']:
                if processes[i] not in ready_queue:
                    ready_queue.append(processes[i])

        isPopped = False
        if ready_queue[current_proc]['remaining_time'] > 0 and ready_queue[current_proc]['remaining_time'] <= quantum:
            current_time += ready_queue[current_proc]['remaining_time']
            ready_queue[current_proc]['remaining_time'] = 0
            processes[ready_queue[current_proc]['id']-1]['isExecuted'] = True
            print("Process", ready_queue[current_proc]['id'])
            processes[ready_queue[current_proc]['id'] -
                      1]['completion_time'] = current_time
            processes[ready_queue[current_proc]['id']-1]['turnaround_time'] = processes[ready_queue[current_proc]
                                                                                        ['id']-1]['completion_time'] - processes[ready_queue[current_proc]['id']-1]['arrival_time']
            processes[ready_queue[current_proc]['id']-1]['waiting_time'] = processes[ready_queue[current_proc]
                                                                                     ['id']-1]['turnaround_time'] - processes[ready_queue[current_proc]['id']-1]['burst_time']
            total_wt += processes[ready_queue[current_proc]
                                  ['id']-1]['waiting_time']
            total_tt += processes[ready_queue[current_proc]
                                  ['id']-1]['turnaround_time']
            ready_queue.pop(current_proc)
            isPopped = True

        elif ready_queue[current_proc]['remaining_time'] > 0:
            ready_queue[current_proc]['remaining_time'] -= quantum
            current_time += quantum
            print("Process", ready_queue[current_proc]['id'])

        for i in range(n):
            if processes[i]['arrival_time'] <= current_time and not processes[i]['isExecuted']:
                if processes[i] not in ready_queue:
                    ready_queue.append(processes[i])

        if isPopped and current_proc > len(ready_queue) - 1:
            current_proc = 0
        elif not isPopped:
            if current_proc < len(ready_queue) - 1:
                current_proc += 1
            else:
                current_proc = 0

    print("\nProcesses     Burst Time     Arrival Time  Waiting Time  Turn-Around Time  Completion Time")
    for i in range(n):
        print(processes[i]['id'], "\t\t",
              processes[i]['burst_time'], "\t\t",
              processes[i]['arrival_time'], "\t\t",
              processes[i]['waiting_time'], "\t\t",
              processes[i]['turnaround_time'], "\t\t",
              processes[i]['completion_time'], "\t\t")
    print("Average waiting time: ", total_wt/n)
    print("Average turn-around time: ", total_tt/n)


if __name__ == '__main__':
    main()
