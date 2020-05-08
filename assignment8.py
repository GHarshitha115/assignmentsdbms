Note: You can make use of imdb.sqlite3 database given to solve this assignment

# Submission Guidelines
Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_008. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_008/
#Coding Guidelines
Write your queries query.py
Query for each question is to be assigned to a variable in the above python file. Variables for each question are specified individually.
#Questions
Get all Budding directors - Find all directors who didn’t direct any film before 2000 and have directed at least one film after 2000. Your query should result in id and fname of the director in ascending order of id.

Sample Output Format:

1 Director1
2 Director2

Query Submission Format:

Q1="Write your query here"


Find the best ranked movie for each director. Incase of more than one movie select the first one when sorted in ascending order of movie name.
Your query should return fname and name of the movie. Your query should return only 100 entries

Sample Output Format:

Director1 Movie1
Director2 Movie2

Query Submission Format:

Q2="Write your query here"

List 100 actors who didn't act in any movie between 1990 and 2000. Your query should return only 100 unique actors when sorted by id in descending order.

Q3="Write your query here"    


ANSWER:

Q1='''
select d.id,d.fname from director as d
where exists(
select m.id from moviedirector inner join movie m
on `m`.id=`moviedirector`.mid 
where m.year > 2000 and d.id=`moviedirector`.did
)
and not exists(
select m.id from moviedirector inner join movie m
on `m`.id=`moviedirector`.mid 
where m.year < 2000 and d.id=`moviedirector`.did
)
order by d.id ASC;
'''
Q2='''
select d.fname,
(
select name from moviedirector inner join movie on
`movie`.id=`moviedirector`.mid 
where `moviedirector`.did=`d`.id
order by rank DESC,name ASC limit 1
)
from director as d limit 100;
'''
Q3='''
select * from  actor a
where not exists(
select m.id from cast inner join movie m
on `m`.id=`cast`.mid
where m.year between 1990 and 2000 and a.id=`cast`.pid
)order by a.id DESC limit 100;
'''





