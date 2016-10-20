

import os.path
import sys

if(sys.argv[1]=="create()"):
	fo = open("birthday.txt","a")
	
	def create():
		bday=raw_input("Bithday?")
		person=raw_input("Whose?")
		fo.write("%s %s") %(bday,person)
	
	eval(sys.argv[1])
	fo.close()

elif not(os.path.isfile("birthday.txt")):
   print "Birthday file does not exist. Please create file."


elif(sys.argv[0]==1):
	fo = open("birthday.txt","r")
	import time
	day=time.strftime("%d/%m")
	flag=0
	while fo.read() is not None:
		line=fo.readline()
		if (day==line[0:6]):
			flag=1
			bday_person=line[6:]
			break
	if (flag==1):
		print "There is %s's birthday today" %(bday_person)
        elif(flag==0):
		print "No birthday today"
	fo.close()

		






