#vivekIOT-Pydev * playfair encrypting coding
#created on 8-7-2017 by Pydev
class cipher():

	def _5x5_matrix(self):
		print self.mylist[1:6]
		print self.mylist[6:11]
		print self.mylist[11:16]
		print self.mylist[16:21]
		print self.mylist[21:26]

	def __init__(self,initial):
		self.mylist=[initial]
		self.msglist=[]
		self.cipher=[]
		self.list1,self.list2,self.list3,self.list4,self.list5=[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]
	
	def content_splitter(self,text):
		for a in text:
			num=len(self.msglist)
			self.msglist.append(a)
		for i in range(0,len(self.msglist)-1):
			if self.msglist[i]==self.msglist[i+1]:
				if self.msglist.index(self.msglist[i+2])%2==0:
					self.msglist.insert(i+1,'x')
		if len(self.msglist)%2!=0:
			self.msglist.append('x')

	def encrypt(self):
		i=1
		while(i<len(self.msglist)):
			val1=self.msglist[i]
			val2=self.msglist[i-1]
			row=self.mylist.index(val1)
			column=self.mylist.index(val2)
			row_pos=(row%5)
			col_pos=(column%5)
			#if row_pos<col_pos:				
			if ((row in self.list1 and column in self.list1) or (row in self.list2 and column in self.list2) or(row in self.list3 and column in self.list3) or(row in self.list4 and column in self.list4) or (row in self.list5 and column in self.list5)):
				if column%5!=0:
					self.cipher.append(self.mylist[column+1])
				else:
					self.cipher.append(self.mylist[column-4])
				if row%5!=0:
					self.cipher.append(self.mylist[row+1])	
				else:
					self.cipher.append(self.mylist[row-4])
			elif(row-column==5 or row-column==-5):
				if ((column in self.list4) and (row in self.list5)):
					self.cipher.append(self.mylist[column+5])
					self.cipher.append(self.mylist[row-20])					
				else:
					self.cipher.append(self.mylist[column+5])
					self.cipher.append(self.mylist[row+5])				
			else:
				if(row-column==6 or row-column==-6):
					self.cipher.append(self.mylist[column+4])
					self.cipher.append(self.mylist[row-4])	
				else:
					self.cipher.append(self.mylist[column+(row_pos-col_pos)])
					self.cipher.append(self.mylist[row-(-col_pos+row_pos)])
			i=i+2
key=raw_input("Enter the key value...")
text=raw_input("Enter the message to encrypt...")
c=cipher('j')
c.content_splitter(text)
alpha="abcdefghiklmnopqrstuvwxyz"
for a in key:
	if a not in c.mylist:
		c.mylist.append(a)
for x in alpha:
	if x not in c.mylist:
		c.mylist.append(x)
c._5x5_matrix()
print "Plain text :"
print c.msglist
c.encrypt()
print "Cipher text :"
print c.cipher

#--------------------------------end of code ---------------------------