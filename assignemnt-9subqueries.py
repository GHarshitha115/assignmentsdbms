Tables:

Team
Match
Player
MatchTeamDetails:
MatchCaptain
GoalDetails
Coding Guidelines:

Write your queries in query.py
Query for each question is to be assigned to a variable in the above metioned python file.
# Query Submission Guideline
Assign your query string to a variable with name have the following format

Q{question Number}="Write your query here"

Below are variable names for question 1 and 2 queries

Q1="Write your query here"
Q2="Write your query here"

#Questions
# Task 1
Get the average age of all the players in the database - [2 Points]

# Sample Output Format
3.245989213123125123

# Task 2
Get match_no and play_date of all the matches which have more than 50000 audience - [2 Points]
Your query should return match_no, play_date in ascending order of match_no.

# Sample Output Format
1	2016-06-11
2	2016-02-12
3	2018-02-01

# Task 3
Get the team_id and the number of matches the team has won for each team in the database (Only consider teams which have played atleast one match) - [2 Points]
Your query should return in the descending order of the number of matches won and then in the ascending ordering of team_id

# Sample Output Format
10012	4
10013	3
10014	0

# Task 4
Get the match_no, play_date for all matches whose stop1_sec is greater than average stop1_sec across all matches - [3 Points]
Your query should return match_no and play_date in descending order of match_no

# Sample Output Format
  3	2016-06-11
  2	2016-04-11
  1	2016-02-11

# Task 5
Get the team names and their captain names for all the matches in the database - [3 Points]
Your query should return match_no, team name and the captain name in ascending order of match_no and team name

# Sample Output Format
1	UK	Rob
1	USA	Mike
3	UK	John

# Task 6
Get the name of the player_of_the_match and his/her jersey_no for all the matches in the database - [3 Points]
Your query should result in match_no, player name and his/her jersey_no in ascending order of match_no

# Sample Output Format
 1	Mike	6
 2	Rob	8
 3	Pike	1

# Task 7
Get the team name and the average age of players in that team for all the teams whose average age is greater than 26 - [3 Points]
Your query should result in team name and average_age in ascending order of name

# Sample Output Format
UK	38.3
USA	27.5

# Task 8
Get the total number of goals scored by all players whose age is less than or equal to 27 - [3 Points]
Your query should return player name, jersey_no, age and the number of goals scored in the descending order of the number of goals and then ascending order of player name. (Consider only the players who scored atleast one goal)

# Sample Output Format
Rob	4	23	8
Pike	3	21	6
John	1	22	3

# Task 9
Get the percentage of goals each team has scored. - [5 Points]
percentage of goals scored by a team = (total number of goals scored by the team across all matches * 100) / total number of goals scored by all the teams acrosss all matches
Your query should return the team_id and the percentage of goals. (Consider only the teams which scored atleast one goal)

# Sample Output Format
   1	9.41234..
   2	30.58766..
   3	60.0

# Task 10
Get the average of total number of goals scored by a team across all the matches - [5 Points]

# Sample Output Format
1.8

# Task 11
Get all the players who didn’t score in any of the matches. - [5 Points]
Your query should return player_id, name and date_of_birth in the ascending order of player_id.

# Sample Output Format
1	Rob	1989-03-10	 
2	Mike	1989-03-10	 
3	Bob	1989-03-10	 

# Task 12
Get the audience count and the difference between the audience count and the teams average audience count for all matches in the database. - [7 Points]
Your query should return team_name, match_no, audience and the difference beteween the audience and the average audience across all matches played by that team in the ascending order of match_no

# Sample Output Format
USA	1	300000   12340
UK	2	123123  12340
Germany	3	123523  12340




ANSWER:


.schema

'''CREATE TABLE Team(
    team_id INTEGER PRIMARY KEY,
    name VARCHAR(40)
);
CREATE TABLE Player(
    player_id integer PRIMARY KEY, 
    team_id integer, 
    jersey_no integer, 
    name VARCHAR(40), 
    date_of_birth DATE, 
    age integer,
    FOREIGN KEY (team_id)        
    REFERENCES Team (team_id)     
            ON DELETE CASCADE     
            ON UPDATE NO ACTION
);
CREATE TABLE Match(
    match_no integer PRIMARY KEY, 
    play_date VARCHAR(40), 
    results VARCHAR(40), 
    goal_score integer, 
    audience integer, 
    player_of_match VARCHAR(40), 
    stop1_sec integer, 
    stop2_sec integer, 
    FOREIGN KEY (player_of_match) 
    REFERENCES Player (player_id) 
);
CREATE TABLE MatchTeamDetails(
    match_no integer, 
    team_id  integer,
    win_lose VARCHAR(10),
    goal_score integer,
    FOREIGN KEY (match_no)  REFERENCES Match(match_no) ON DELETE CASCADE ON UPDATE NO ACTION, 
    FOREIGN KEY (team_id) REFERENCES  Team(team_id) ON DELETE CASCADE ON UPDATE NO ACTION
);
CREATE TABLE MatchCaptain(  
    match_no integer,  
    team_id integer, 
    captain integer,   
    FOREIGN KEY (match_no) REFERENCES Match (match_no)  ON DELETE CASCADE ON UPDATE NO ACTION, 
    FOREIGN KEY (team_id) REFERENCES Team (team_id) ON DELETE CASCADE ON UPDATE NO ACTION, 
    FOREIGN KEY (captain) REFERENCES Player (player_id) ON DELETE CASCADE ON UPDATE NO ACTION
);
CREATE TABLE GoalDetails(
    goal_id integer PRIMARY KEY, 
    match_no integer, 
    player_id integer, 
    team_id integer, 
    goal_time VARCHAR(40), 
    FOREIGN KEY (match_no) REFERENCES Match (match_no) ON DELETE CASCADE ON UPDATE NO ACTION, 
    FOREIGN KEY (player_id) REFERENCES Player (player_id) ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (team_id) REFERENCES Team (team_id) ON DELETE CASCADE ON UPDATE NO ACTION
);
CREATE INDEX team_team_id ON Team(team_id);
CREATE INDEX team_name ON Team(name);
CREATE INDEX player_name ON Player(name);
CREATE INDEX player_player_id ON Player(player_id);
CREATE INDEX player_age ON Player(age);
CREATE INDEX player_team_id ON Player(team_id);
CREATE INDEX match_captain_match_no ON MatchCaptain(match_no);
CREATE INDEX match_captain_team_id ON MatchCaptain(team_id);
CREATE INDEX match_captain_captain ON MatchCaptain(captain);
CREATE INDEX match_match_no ON Match(match_no);
CREATE INDEX match_goal_score ON Match(goal_score);
CREATE INDEX match_player_of_match ON Match(player_of_match);
CREATE INDEX match_team_details_match_no ON MatchTeamDetails(match_no);
CREATE INDEX match_team_details_team_id ON MatchTeamDetails(team_id);
CREATE INDEX goal_details_goal_id ON GoalDetails(goal_id);
CREATE INDEX goal_details_match_no ON GoalDetails(match_no);
CREATE INDEX goal_details_player_id ON GoalDetails(player_id);
CREATE INDEX goal_details_team_id ON GoalDetails(team_id);
'''


Q1="select avg(age) from Player "
Q2="select match_no,play_date from Match where audience>50000 "
Q3='''
select team_id,count(win_lose) as c
from matchteamdetails 
where win_lose='W' group by team_id order by c DESC,team_id ASC;
'''
Q4='''
select match_no,play_date from Match
where stop1_sec >
(
select avg(stop1_sec)
from match
) 
order by match_no DESC;
'''

Q5='''
select match_no,team.name,player.name from matchcaptain
inner join team on matchcaptain.team_id=team.team_id
inner join player on matchcaptain.captain=player.player_id
order by matchcaptain.match_no,team.name;
'''

Q6 = '''
select match_no,player.name,player.jersey_no 
from match 
inner join player on match.player_of_match = player.player_id 
order by match_no ASC;
'''
Q7 ='''
select team.name,avg(player.age) as average_age 
from player inner join team on player.team_id = team.team_id	
group by team.name having avg(player.age)>26 order by team.name ASC;
'''

Q8='''
select name,jersey_no,age,count(goal_id) as c
from player inner join goaldetails on goaldetails.player_id=player.player_id
where age<=27 group by goaldetails.player_id order by c DESC,
player.name ASC;
'''


Q9='''
select team_id,count(goal_id)*100.0
/(
select count(goal_id) from goaldetails 
) from goaldetails group by team_id;
'''

Q10='''
select AVG(s) from
(select count(goal_id) as s from goaldetails group by team_id);
'''

Q11='''
select player.player_id,name,date_of_birth from player 
where not exists (select player_id
from goaldetails where player.player_id=goaldetails.player_id);
'''
Q12='''
select name,m.match_no,audience,audience-
(
select avg(audience) from match
join matchteamdetails as mt on mt.match_no=match.match_no where mt.team_id=t.team_id)
from match as m
inner join matchteamdetails as mtd on mtd.match_no=m.match_no
inner join team as t on t.team_id=mtd.team_id
order by m.match_no ASC
;
'''
