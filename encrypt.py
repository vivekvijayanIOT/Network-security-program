#vivekIOT encrypting coding
from string import maketrans
intab="abcdefghijklmnopqrstuvwxyz"
outtab="bcdefghijklmnopqrstuvwxyza"
a=0
b=0
key_run=maketrans(intab,outtab)
string=raw_input("Enter the string to be encrypted\n")
key=input("Enter the key\n")
while a<key:
	string=string.translate(key_run)
	a=a+1
print "Data is encrypted as :"
print string
print "\n\n"
word_to_decode=raw_input("Enter the string to decode\n")
decode_run=maketrans(outtab,intab)
key2=input("Enter the decode key\n")
while b<key2:
	word_to_decode=word_to_decode.translate(decode_run)
	b=b+1
print "Data is decrypted as :"
print word_to_decode
