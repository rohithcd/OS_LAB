for i in range(n):
    x=int(input("Enter the process : "))
    myList[i]['processes']=x
    y=int(input(f"Enter the BurstTime of process{x} : "))
    myList[i]['BurstTime']=y
    z=int(input(f"Enter the ArrivalTime of process{x} : "))
    myList[i]['ArrivalTime']=z