QUESTION:

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
Find all the players in the database who acted as captain for at-least one match and didn't make at least one goal.

# Sample Output Format
player_id|team_id|jersey_no|name|date_of_birth|age
160140|1207|1|Hugo Lloris|1986-12-26|29
160349|1216|6|Vlad Chiriches|1989-11-14|26
160013|1201|5|Lorik Cana|1983-07-27|32
160467|1221|2|Stephan Lichtsteiner|1984-01-16|32
160401|1218|3|Martin Skrtel|1984-12-15|31
..............
# Task 2
Find the number of games played by each team

# Sample Output Format
team_id|no_of_games
1201|3
1202|3
1203|5
1204|4
1205|3
........
# Task 3
Find the average goal score of each team. The average goal score for a team is the total number of goals divided by the total number of members in the team.

# Sample Output Format
team_id|avg_goal_score
1201|0.0434782608695652
1202|0.0434782608695652
1203|0.391304347826087
1204|0.217391304347826
1205|0.0869565217391304
.......
# Task 4
For each captain find the number of matches he/she has been captain to that match. The result should have captain and no_of_times_captain columns as shown below.

# Sample Output Format
captain|no_of_times_captain
160004|2
160013|1
160028|3
160062|5
160076|4
...........
# Task 5
Find the number of players(no_players) who are captain and also awarded the player of the match for the same match.

# Sample Output Format
no_players
6
# Task 6
Find the distinct player ids who are captain for atleast one match and didn't get the player of the match title for even a single match.

# Sample Output Format
captain
160004
160004
........
# Task 7
Find the number of matches played in each month. Your query should return Month and no_of_matches in the descending order of no_of_matches

# Sample Output Format
month|no_of_matches
06|44
...
# Task 8
Find the jersey number and the number of captains use it. Your query should return jersey_no and no_captains in the descending order of no_captains and jersey_no.

# Sample Output Format
jersey_no|no_captains
1|17
....
# Task 9
Find the average of the audience for each player. In the descending order of avg_audience and player_id.

# Sample Output Format
player_id|avg_audience
160001|49075.66
160002|145675.123
160003|97234.66
160004|72345.852
160005|91203.123
...
# Task 10
Calculate the average age of players for each team.

# Sample Output Format
team_id|AVG(age)
1201|27.0869565217391
1202|27.2173913043478
1203|25.9130434782609
1204|26.304347826087
1205|28.7391304347826
......... 

# Task 11
Calculate the average age of all the captains in the database.

# Sample Output Format
avg_age_of_captains
30.6078431372549	 

# Task 12
Find the month and the number of players born in that month in the descending order of no_of_players and month.

# Sample Output Format
month|no_of_players
01|59
....
# Task 13
Find the captain id and the number of matches he/she has won(no_of_wins). Your Query should return captain and no_of_wins in the descending order of no_of_wins.

# Sample Output Format
captain|no_of_wins
160140|5
160163|4
160322|4
160539|4
160062|3
.........





ANSWER:

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

Q1='''
select p.player_id,mt.team_id,p.jersey_no,p.name,p.date_of_birth,p.age
from player p inner join matchcaptain mt on
mt.captain=p.player_id
left join goaldetails on goaldetails.player_id=mt.captain
where goal_id is null;
'''

Q2='''
select team_id,count(match_no) from matchteamdetails group by team_id
'''

Q3='''
select team.team_id,
(select count(goal_id) from goaldetails where goaldetails.team_id=team.team_id)/
CAST((select count(player_id) from player where player.team_id=team.team_id) AS FLOAT)
from goaldetails inner join team on goaldetails.team_id=team.team_id
group by team.team_id;
'''

Q4='''
select captain,count(player_id) from matchcaptain
inner join player on matchcaptain.captain=player.player_id
group by captain
'''

Q5='''
select count(DISTINCT(captain)) from match
inner join matchcaptain on
match.match_no=matchcaptain.match_no
where match.player_of_match=matchcaptain.captain
'''
Q6='''
select DISTINCT(p.player_id)
from player p
where exists(
select mt.captain from matchcaptain mt where p.player_id=mt.captain
)
and not exists
(
select match.player_of_match from match where match.player_of_match=p.player_id
)
'''

Q7='''                                     
select strftime('%m',play_date) as month,count(match_no) as no_of_matches
from match
group by month order by no_of_matches DESC;
'''

Q8='''
select jersey_no,count(captain) as no_captains from player
inner join matchcaptain where player.player_id=matchcaptain.captain
group by jersey_no order by no_captains DESC,jersey_no DESC;
'''

Q9='''
select player_id,avg(audience) as avg_audience from player inner join matchteamdetails
on player.team_id=matchteamdetails.team_id
inner join match on match.match_no=matchteamdetails.match_no
group by player_id
order by avg_audience DESC,player_id DESC;
'''

Q10='''
select player.team_id,avg(age) from player 
inner join matchteamdetails on matchteamdetails.team_id=player.team_id
group by player.team_id;
'''

Q11='''
select avg(age) from player inner join matchcaptain on 
player.player_id=matchcaptain.captain
;
'''

Q12='''
select strftime('%m',date_of_birth) as month,count(player_id) as no_of_players
from player
group by month order by no_of_players DESC,month DESC;
'''

Q13='''
select captain,count(win_lose) as no_of_wins
from matchcaptain inner join matchteamdetails on
matchcaptain.match_no=matchteamdetails.match_no
where win_lose='W' and matchcaptain.team_id=matchteamdetails.team_id
group by captain order by no_of_wins DESC;
'''
