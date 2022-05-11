import os
r,w=os.pipe()
r1,w1=os.pipe()
pid=os.fork()

def leapYear(y):
	year=int(y)
	if(year%400==0 and year%100==0):
		return ("Leap year")
	elif(year%4==0 and year%100!=0):
		return ("Leap year")
	else:
		return ("Not Leap year")

if pid:
	os.close(r)
	w=os.fdopen(w,'w')
	
	year=input("Enter year :")
	
	w.write(year)
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
	y=r.read()
	
	x=leapYear(y)
	
	w1.write(x)
	w1.close()
	r.close()
