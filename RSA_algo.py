from random import randint
import math
def gcd(a,b):
	if b > a:
		if b % a == 0:
            		return a
        	else:
            		return gcd(b % a, a)
    	else:
        	if a % b == 0:
           	 	return b
        	else:
        		return gcd(b, a % b)  

print "***************RSA ALGORITHM*******************"
p=input("\nEnter the value of p = ")
q=input("\nEnter the value of q = ")
if (p==q):
	print "P and Q are equal"
else:
	n=p*q;
	pon=(p-1)*(q-1)
	e=randint(0,pon)
	f=gcd(e,pon)
	while(f!=1):
		e=randint(0,pon)
		f=gcd(e,pon)
	print "\n\ne value found as %d"%e
	print "\n Finding d ....\n"
	d=1
	ans=0
	while(ans!=1):
		d=d+1
		ans=(d*e)%pon
		
	print "\nd value found as %d"%d
	print "\nRSA IS READY >>>>>\n\n"
	msg=input("Enter the plain message = ")
	cipher=(int(math.pow(msg,e))%n)
	print "Cipher text is %d"%cipher
	
	msg1=cipher
	pt=(int(math.pow(msg1,d))%n)
	print "Original text is %d"%pt
	 
	
	
