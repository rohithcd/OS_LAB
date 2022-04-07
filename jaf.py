from operator import itemgetter
import pandas as pd
#for sorted func

n=int(input("Enter the number of processes"))
#for the number of processes from the user

process = []
#creating an empty list

#for accepting arrival time and burst time
for i in range(n):
	p_id = "p"+str(i+1)
	a_time = int(input("Enter the arrival time for process"+str(i+1)+":"))
	#%d as placeholder for real and integers and %s for string
	b_time = int(input("Enter the burst time for process"+str(i+1)+":"))
	process.append({'pid':p_id,'atime':a_time,'btime':b_time,'ctime':0,'wtime':0,'tatime':0})
	
#sorting the process according to arrival time
process=sorted(process,key=itemgetter('atime'))

to_wtime=0
to_tatime=0
#assigning the values for the first process
process[0]['ctime'] = process[0]['atime']+process[0]['btime']
process[0]['tatime'] = process[0]['ctime']-process[0]['atime']
process[0]['wtime'] = 0
to_tatime = to_tatime+process[0]['tatime'] 
i=1

#calculating values for each process
while (i<n):
	#if there no gap/delay between two process
	if process[i-1]['ctime']>process[i]['atime']:
		process[i]['ctime'] = process[i]['btime']+process[i-1]['ctime']
	#if there is gap/delay between two process
	else:
		process[i]['ctime'] = process[i]['btime']+process[i]['atime']
	process[i]['tatime'] = process[i]['ctime']-process[i]['atime']
	to_tatime = to_tatime+process[i]['tatime'] 
	process[i]['wtime'] = process[i]['tatime']-process[i]['btime']
	to_wtime=to_wtime+process[i]['wtime']
	i=i+1
process=pd.DataFrame(process)
print(process)
print("the average waiting time is ",(to_wtime/n))
print("the average turnaround time is ",(to_tatime/n))