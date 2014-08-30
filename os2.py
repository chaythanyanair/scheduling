#!/usr/bin/python
import sys
import os.path
def initialise(choice,filename):
	f=open(filename)
	my_list=[]
	for i in f:
		my_list.append(i.strip())
	n=int((my_list[0].split(':'))[1])
	time_slot=int((my_list[1].split(':'))[1])
	overhead=int((my_list[2].split(':'))[1])
	process_list=[]
	for value in my_list:
		if len(value)!=0:
			if (value.split(':'))[0]=='PROCESS':
				process_list.append(value)
	if choice==2 or choice==4:
		process_list.sort(key=lambda(x): int((x.split(':'))[3]))
	process_names=[(x.split(':'))[1] for x in process_list]
	process_times=[(x.split(':'))[2] for x in process_list]
	process_times=[int(x) for x in process_times]
	process_arrival=[(x.split(':'))[3] for x in process_list]
	process_arrival=[int(x) for x in process_arrival]
	done=[]
	index=0
	for i in range(n):
		done.append(True)
	flag=0
	if choice==1 or choice==3 :
		wona(n,process_list,process_names,process_times,time_slot,f,index,done,flag,overhead,choice)
	elif choice==2 or choice==4:
		wowa(n,process_list,process_names,process_times,process_arrival,time_slot,f,index,done,flag,overhead,choice)
	elif choice==5:
		sys.exit()
	else:
		print 'wrong choice!!'
def print_time(turn_around,wait_time,o,n):
	print "\nScheduled and output written to file!\n"	
	for i in range(len(turn_around)):
		o.write('TRnd('+str(turn_around.items()[i][0])+') = '+str(turn_around.items()[i][1])+'\n')
	turn_avg=reduce(lambda x,y:x+y,turn_around.values())/float(len(turn_around))
	o.write('Average TRnd time:'+str(turn_avg)+'\n')
	for i in range(len(wait_time)):
		o.write('W('+str(wait_time.items()[i][0])+') = '+str(wait_time.items()[i][1])+'\n')	
	wait_avg=reduce(lambda x,y:x+y,wait_time.values())/float(len(wait_time))
	for i in range(n):
		o.write('\nW('+str(i)+') ='+str(wait_time[i]))
	o.write('Average Wait time:'+str(wait_avg))
def wowa(n,process_list,process_names,process_times,process_arrival,time_slot,f,index,done,flag,overhead,choice):
	if choice==4:
		o=open('with_overhead_and_arrival.txt','wb')
		o.write('\t\tCONSIDERING BOTH OVERHEAD AND ARRIVAL TIME\n')
	elif choice==2:
		o=open('no_overhead_with_arrival.txt','wb')
		o.write('\t\tWITHOUT CONSIDERING OVERHEAD BUT ARRIVAL TIME\n')
	turn_around={}
	wait_time={}
	i=0	
	while i<n:
		while done[i]==True and index>=process_arrival[i]:
			if not(str(process_names[i]) in wait_time):
				c=index-process_arrival[i]
                		wait_time.update({str(process_names[i]):c})
			flag=0
			index1=index
			if(process_times[i]<time_slot):
				index+=(process_times[i])
				done[i]=False
				o.write(str(index1)+ ':'+str(process_names[i])+':'+str(process_times[i])+':COMPLETED\n')
				process_times[i]=0				
				turn_around.update({str(process_names[i]):(index-process_arrival[i])})
				process_arrival.remove(process_arrival[i])
        	       		process_times.remove(process_times[i])
				process_names.remove(process_names[i])
				done.remove(done[i])
				i=i-1
		               	n=n-1
				flag=1
			else:
				index+=(time_slot)
				process_times[i]=process_times[i]-time_slot
				if process_times[i]==0:
				        done[i]=False
					o.write(str(index1)+ ':'+str(process_names[i])+':'+str(time_slot)+':COMPLETED\n')
					turn_around.update({str(process_names[i]):(index-process_arrival[i])})
					process_times.remove(process_times[i])
					process_names.remove(process_names[i])
					process_arrival.remove(process_arrival[i])
					done.remove(done[i])
					
					i=i-1
			      		n=n-1
					flag=1
			if flag==0:
				 o.write(str(index1)+ ':'+str(process_names[i])+':'+str(time_slot)+':NOT COMPLETED\n')
			i=i+1
			if choice==4:
				if True in done:
					o.write(str(index)+':scheduler:'+str(overhead)+'\n')
				index=index+overhead
			if i==n:
				break
		if i<n and index<process_arrival[i]:
			i=0
		elif i==n and True in done:
			i=0	
		else:
			i=i+1
	print_time(turn_around,wait_time,o,n)
	o.close()
	f.close()
def wona(n,process_list,process_names,process_times,time_slot,f,index,done,flag,overhead,choice):
	if choice==3:
		o=open('with_overhead_no_arrival.txt','wb')
		o.write('\t\tCONSIDERING OVERHEAD BUT NOT ARRIVAL TIME\n') 
	elif choice==1:
		o=open('no_overhead_or_arrival.txt','wb')
		o.write('\t\tWITHOUT CONSIDERING OVERHEAD OR ARRIVAL TIME\n') 
	turn_around={}
	wait_time={}
	i=0
	while i<n:
		while done[i]==True:
			if not(str(process_names[i]) in wait_time):
				wait_time.update({str(process_names[i]):index})
			flag=0
			index1=index
			if(process_times[i]<time_slot):
				index+=(process_times[i])
				done[i]=False
				o.write(str(index1)+ ':'+str(process_names[i])+':'+str(process_times[i])+':COMPLETED\n')
				process_times[i]=0
				turn_around.update({str(process_names[i]):index})
				process_times.remove(process_times[i])
				process_names.remove(process_names[i])
				done.remove(done[i])
				i=i-1
		               	n=n-1
				flag=1
			else:
				index+=(time_slot)
				process_times[i]=process_times[i]-time_slot
				if process_times[i]==0:
				        done[i]=False
					o.write(str(index1)+ ':'+str(process_names[i])+':'+str(time_slot)+':COMPLETED\n')
					turn_around.update({str(process_names[i]):index})
					process_times.remove(process_times[i])
					process_names.remove(process_names[i])
					done.remove(done[i])
					i=i-1
			      		n=n-1
					flag=1				
			if flag==0:
				o.write(str(index1)+ ':'+str(process_names[i])+':'+str(time_slot)+':NOT COMPLETED\n')
			i=i+1
			if choice==3:
				if True in done:
					o.write(str(index)+':scheduler:'+str(overhead)+'\n')
				index=index+overhead
			if i==n:
				break		
		if i==n and True in done:
			i=0	
		else:
			i=i+1
	print_time(turn_around,wait_time,o,n)
	o.close()
	f.close()
if __name__=="__main__" :
	if len(sys.argv) >2:
		raise Exception("Too Many Arguments Passed")
	else:
		if os.path.isfile(str(sys.argv[1])):
			while True:
				print 'ROUND ROBIN SCHEDULLING'
				print '1- Without considering overhead or arrival time'
				print '2- without considering overhead but arrival time'
				print '3- considering overhead and not arrival time'
				print '4- considering both overhead and arrival time'
				print '5-exit'
				choice=input('Please enter your choice:')
				initialise(choice,sys.argv[1])		
			
		else:
			raise Exception("FileNotFoud!!")

