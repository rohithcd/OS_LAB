#child read parent reverse and write child display

import os
r,w = os.pipe()
r1,w1 = os.pipe()
pid = os.fork()

if pid:
	os.close(w)
	os.close(r1)
	w1=os.fdopen(w1,'w')
	r=os.fdopen(r)
	x=r.read()
	x=x[::-1]
	w1.write(x)
	w1.close()
	r.close()
else:
	os.close(r)
	w=os.fdopen(w,'w')
	wo=input("Enter the string:")
	print(f"child taken the input: {wo}")
	
	w.write(wo)
	w.close()
	os.close(w1)
	r1=os.fdopen(r1)
	y=r1.read()
	print(f"parent read the reverse string :{y}")
	r1.close()
