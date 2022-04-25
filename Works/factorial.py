import os

r,w=os.pipe()
r1,w1=os.pipe()
pid=os.fork()



def factorial(n):
	n=int(n)

	fact=1
	
	for i in range(1,n+1):
		fact=fact*i
	fact=str(fact)	
	return fact
		

	

if pid:
	os.close(r)
	
	w=os.fdopen(w,'w')
	
	n=input("Enter the number:")
	
	
	w.write(n)
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
	
	w1=os.fdopen(w1,'w')
	b=r.read()
	print(f"child read: {b}")
	
	fact=factorial(b)
	
	w1.write(fact)
	
	w1.close()
	
	r.close()


	
	
