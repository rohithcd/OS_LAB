import os

r,w=os.pipe()
r1,w1=os.pipe()
pid=os.fork()



def armstrong(n):
	num=int(n)
	
	cube=0
	
	for i in n:
		i=int(i)
		cube=cube+pow(i,3)
	if(cube==num):
		return(f"{num} is Armstrong NUmber")
	else:
		return (f"{num} is not Armstrong NUmber")
		

	

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
	
	fact=armstrong(b)
	
	w1.write(fact)
	
	w1.close()
	
	r.close()


	
	
