import os
r,w = os.pipe()
r1,w1 = os.pipe()
pid = os.fork()




if pid:
	os.close(r)
	w = os.fdopen (w,'w')

	x=input("Enter the string: ")
	print( "Parent writes =", x)
		
	w.write(x)
	w.close()
	
	os.close(w1)
	r1 = os.fdopen(r1)
	
	y1= r1.read()
	print("Parent reads string = ",y1)
		
	r1.close()

else:

	os.close(w)
	os.close(r1)
	
	r = os.fdopen(r)
	y = r.read()
	r.close()
	
	w1 = os.fdopen (w1,'w')
	
	if y==y[::-1]:
	
		print("Child checks palindrome = ",y)
		w1.write(str("The string is Palindrome"))
		
	else:
		print("Child checks palindrome = ",y)
		w1.write(str("The string is not a Palindrome"))
	w1.close()
			
			
		
		
	
	
	
	
	

