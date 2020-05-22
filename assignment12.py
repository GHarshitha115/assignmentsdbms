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

class DoesNotExist(Exception):
    pass
class InvalidField(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class Student:
    a=''
    b=0
    def __init__(self,name=None,age=None,score=None):
        self.name=name
        self.age=age
        self.student_id=None
        self.score=score
        
    @classmethod
    def get(cls,**keys):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
        for k,v in keys.items():
            cls.a=k
            cls.b=v
        if cls.a not in('student_id','name','age','score'):
            raise InvalidField
        sql_query="select * from Student where {}='{}'".format(cls.a,cls.b)
        crsr.execute(sql_query)       
        ans=crsr.fetchall()
        if (len(ans)==0):
            raise DoesNotExist
        elif(len(ans)>1):
            raise MultipleObjectsReturned
        obj=Student(ans[0][1],ans[0][2],ans[0][3])
        obj.student_id=ans[0][0]
        conn.close()
        return obj
    @classmethod  
    def delete(cls):
        sql_query="delete from Student where {}={}".format(cls.a,cls.b)
        write_data(sql_query)
    def save(self):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
        crsr.execute("PRAGMA foreign_keys=on;")
        if self.student_id==None:
            sql_query="INSERT INTO Student(name,age,score)values('{}',{},{})".format(self.name,self.age,self.score)
            crsr.execute(sql_query)
            self.student_id=crsr.lastrowid
        else:
            sql_query="UPDATE Student SET name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.student_id)
            crsr.execute(sql_query)
        conn.commit()
        conn.close()
        
        '''

        another method:
        
        if self.student_id is None:
            query="insert into student(name,age,score)values('{}',{},{})".format(self.name,self.age,self.score)
            write_data(query)
            q1='select student_id from student where name="{}" and age={} and score={}'.format(self.name,self.age,self.score)
            r1=read_data(q1)
            self.student_id=r1[0][0] 

        else:
            query1="update student set name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.b)
            write_data(query1)
	    
	    '''
	    



'''student_object = Student.get(student_id=4)
student_object.name="Vijju"
student_object.save()
print(student_object.student_id)'''
