import os
r,w=os.pipe()
r1,w1=os.pipe()
pid = os.fork()

def even(a):
	li=a.split(',')
	st=""
	li=li[0:len(li)-1]
	for i in li:
		i=int(i)
		if i%2==0:
		
			st=st+str(i)+','
	return st
if pid:

	os.close(r)
	w=os.fdopen(w,'w')
	s=int(input("Enter the number of numbers:"))
	str=""
	for i in range(s):
		i=input()
		str=str+i+','
		
	print("parent writes: ")
	w.write(str)
	w.close()
	os.close(w1)
	r1=os.fdopen(r1)
	s=r1.read()
	print(s)
	r1.close()
	
else:

	os.close(w)
	os.close(r1)
	r=os.fdopen(r)
	b=r.read()
	x=even(b)
	w1=os.fdopen(w1,'w')
	w1.write(x)
	w1.close()
	r.close()
	

	
