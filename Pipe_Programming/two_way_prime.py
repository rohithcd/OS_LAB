import os
r,w = os.pipe()
r1,w1 = os.pipe()
pid = os.fork()

def prime(n):
	count=0
	
	if n!=1:
		for i in range(1,n+1):
			if n%i==0:
				count=count+1
		if count==2:
			return n			
		else:
			return 0			
	else:	
		return 0
			

if pid:
	os.close(r)
	w = os.fdopen (w,'w')
	
	n=(input("Enter the n value: "))

	li=""
	
	for i in range(int(n)):
	
		x=(input("Enter the number: "))
		li=li+x
		print( "Parent writes =", x)
		
	w.write(li)

	w.close()
	
	os.close(w1)
	r1 = os.fdopen(r1)
	
	y1= r1.read()
	
	
	for i in y1:
		print("Parent reads prime number = ",i)
		
	r1.close()
	
else:

	os.close(w)
	os.close(r1)
	
	r = os.fdopen(r)

	y = r.read()
	
	r.close()
	
	w1 = os.fdopen (w1,'w')
	
	li1=""
	for i in y:
		i=int(i)
		p=prime(i)
		
		if p!=0:
			li1=li1+str(p)
			
			print("Child accept the prime number= ",p)
			
	w1.write(li1)
		
	w1.close()
			
			
		
		
	
	
	
	
	
