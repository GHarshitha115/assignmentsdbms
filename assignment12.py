class Student:
    def __init__(self,id=None,name=None,age=None,score=None):
        self.name=name
        self.id=id
        self.age=age 
        self.score=score
    @staticmethod
    def get(sql):
        import sqlite3
        connection=sqlite3.connect("dbms/dbms_resources/students_db.sqlite3")
        crsr=connection.cursor()
        crsr.execute("SELECT * from Student where id=100;")    
        ans=(crsr.fetchone())
        b=Student(*ans)
        connection.close()
        return b
student_obj=Student.get("ID=100")
print(student_obj.name)
