def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()
def read_data(sql_query):
	import sqlite3 
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

class DoesNotExist(Exception):
    pass
class InvalidField(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class Student:
    a=''
    b=0
    c=''
    d=0
    def __init__(self,name=None,age=None,score=None):
        self.name=name
        self.age=age
        self.student_id=None
        self.score=score
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(self.student_id,self.name,self.age,self.score)
    @classmethod
    def get(cls,**keys):
        import sqlite3
        conn=sqlite3.connect("selected_students.sqlite3")
        crsr=conn.cursor()
        for key,value in keys.items():
            cls.a=key
            cls.b=value
        if cls.a not in('student_id','name','age','score'):
            raise InvalidField
        sql_query="select * from Student where {}='{}'".format(cls.a,cls.b)
        crsr.execute(sql_query)       
        ans=crsr.fetchall() 
        if (len(ans)==0):
            raise DoesNotExist
        elif(len(ans)>1):
            raise MultipleObjectsReturned
        else:    
            obj=Student(ans[0][1],ans[0][2],ans[0][3])
            obj.student_id=ans[0][0]
            return obj
            
    @classmethod  
    def delete(cls):
        sql_query="delete from Student where {}={}".format(cls.a,cls.b)
        write_data(sql_query)
    def save(self):
        if self.student_id is None:
            query="insert into student(name,age,score)values('{}',{},{})".format(self.name,self.age,self.score)
            write_data(query)
            query_student_id='select student_id from student where name="{}" and age={} and score={}'.format(self.name,self.age,self.score)
            que=read_data(query_student_id)
            self.student_id=que[0][0]
        else:
            query1="update student set student_id={},name='{}',age={},score={} where student_id={}".format(self.student_id,self.name,self.age,self.score,self.b)
            write_data(query1)
    @classmethod 
    def filter(cls,**keys):
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
        z='select * from student where '+z
        obj=read_data(z)
        for i in range (len(obj)):
             obj1=Student(obj[i][1],obj[i][2],obj[i][3])
             obj1.student_id=obj[i][0]
             cls.objects.append(obj1)
        return cls.objects
        

