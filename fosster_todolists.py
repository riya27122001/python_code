import sys
import time
import sqlite3

i=1

class event(object):
	
	def __init__(self, name=None, desc=None, date=None, p='m'):
		self.name=name
		self.desc=desc
		self.date=date
		self.p=p
	def write(self):
		todo.execute('INSERT INTO ' + cat +
		''' (NAME,DESCIPTION,DATE,PRIORITY)\
		VALUES(self.name,self.desc,self.date,self.p);''')
		todo.commit()
		
	def pr(self):
		print self.name+' '+self.desc+' '+self.date+' '+self.p
		


todo =sqlite3.connect('todo.db')
print "todo database created"
todo.close()

if sys.argv[1]=='add':
	cat=sys.argv[2]
	todo =sqlite3.connect('todo.db')	
	todo.execute('CREATE TABLE '+ cat+' (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, DESCRIPTION TEXT NOT NULL, DATE TEXT NOT NULL, PRIORITY TEXT NOT NULL);')
		          
		          
		          
	print 'Table ' + cat + ' created successfully.'
	todo.close()
	
if sys.argv[1]=='create':
	cat=sys.argv[2]
	name=raw_input('Name of Event?')
	desc=raw_input('Event description?')
	date=raw_input('Date?')
	priority=raw_input('Priority?')
	ev=event(name,desc,date,priority)
	todo=sqlite3.connect('todo.db')
	ev.write()
	print "object added."
	
	todo.close()
	
	
if sys.argv[1]=='list':
	cat=sys.argv[2]
	todo=sqlite3.connect('todo.db')
	lis=todo.execute('SELECT ID,NAME,DESCRIPTION,DATE,PRIORITY FROM '+argv[2]+';')
	print 'ID  NAME	               DESC                    DATE  PRIORITY'
	for row in lis:
		print row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[5]
	todo.close()
	
if sys.argv[1]=='edit':
	cat=sys.argv[2]
	idx=sys.argv[3]
	field=raw_input('Enter field to be updated:')
	val=raw_input('Enter updated value:')
	todo=sqlite3.connect('todo.db')
	todo.execute('UPDATE '+cat+' set '+field+' = '+val+' where ID='+idx+';')
	todo.close()
	
	
if sys.argv[1]=='delete':
	if sys.argv[3]==None:
		tab=sys.argv[2]
		todo=sqlite3.connect('todo.db')
		todo.execute('DROP TABLE '+tab+';')
		todo.close()
	if sys.argv[3]!=None:
		tab=sys.argv[2]
		idx=sys.argv[3]
		todo=sqlite3.connect('todo.db')
		todo.execute('DELETE from '+tab+' where ID='+idx+';')
		
	
	

	
		
	


