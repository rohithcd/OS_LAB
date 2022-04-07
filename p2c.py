import os
r,w = os.pipe()
pid = os.fork()
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
	
else:

	os.close(w)
	r = os.fdopen(r)
	y = r.read()

	for i in y:
		print("Child reads = ",i)
		
	r.close()
	