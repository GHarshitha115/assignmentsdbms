def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()
def read_data(sql_query):
	import sqlite3 
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
class InvalidField(Exception):
    pass
class Student:
	a=''
	b=0
	c=''
	d=0
	m=''
	def __init__(self,name=None,age=None,score=None):
		self.name=name
		self.age=age
		self.student_id=None
		self.score=score
	
	@classmethod
	def avg(cls,field,**kwargs):
		cls.m='avg'
		x=Student.filter(field,**kwargs)
		#print(x)
		return x[0][0]
	@classmethod
	def max(cls,field,**kwargs):
		cls.m='max'
		x=Student.filter(field,**kwargs)
		return x[0][0]
	@classmethod
	def min(cls,field,**kwargs):
		cls.m='min'
		x=Student.filter(field,**kwargs)
		return x[0][0]
	@classmethod
	def sum(cls,field,**kwargs):
		cls.m='sum'
		x=Student.filter(field,**kwargs)
		return x[0][0]
	@classmethod
	def count(cls,field=None,**kwargs):
		#print(field)
		if field is None:
			x='select count(*) from student'
			x=read_data(x)
			return x[0][0]
		else:
			cls.m='count'
			x=Student.filter(field,**kwargs)
			return x[0][0]
	@classmethod 
	def filter(cls,field,**keys):
		if field not in('student_id','name','age','score'):
			raise InvalidField
		cls.objects=[]
		cls.li=[]
		for key,value in keys.items():
			cls.c=key
			cls.d=value
			e=cls.c
			e=e.split("__")
			if e[0] not in('student_id','name','age','score'):
			    raise InvalidField
			if len(e)>1:
				if e[1]=='lt':
					sql_query="{}<{}".format(e[0],cls.d)
				elif e[1]=='lte':
					sql_query="{}<='{}'".format(e[0],cls.d)
				elif e[1]=='gt':
					sql_query="{}>{}".format(e[0],cls.d)
				elif e[1]=='gte':
					sql_query="{}>={}".format(e[0],cls.d)
				elif e[1]=='neq':
					sql_query="{}!='{}'".format(e[0],cls.d)
				elif e[1]=='in':
					sql_query="{} in {}".format(e[0],tuple(cls.d))
				elif e[1]=='contains':
					sql_query="{} like '%{}%'".format(e[0],cls.d)
			elif (len(e))==1:
				sql_query="{}='{}'".format(cls.c,cls.d)
			cls.li.append(sql_query)
			z=' and '.join(cls.li)
		if (len(keys.items()))>=1:
			z='select {}({}) from student where '.format(cls.m,field)+z
		else:
			z='select {}({}) from student'.format(cls.m,field)
		
		obj=read_data(z)
		return obj
		# for i in range (len(obj)):
		# 	obj1=Student(obj[i][1],obj[i][2],obj[i][3])
		# 	obj1.student_id=obj[i][0]
		# 	cls.objects.append(obj1)
		# return cls.objects
        

	
'''
count = Student.count()
print(count)
'''
