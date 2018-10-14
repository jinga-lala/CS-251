import sqlite3

if __name__ == "__main__":
    ipl =sqlite3.connect("ipl.db")
    cur = ipl.cursor()
    cur.execute('''CREATE TABLE TEAM (team_id int,	team_name int, primary key (team_id))''')

    cur.execute('''CREATE TABLE PLAYER (player_id int, player_name varchar(100),  dob timestamp,
    batting_hand varchar(100), bowling_skill varchar(100),	country_name varchar(100),
    primary key (player_id))''')

    cur.execute('''CREATE TABLE MATCH  (match_id int, season_year int,	team1 int,	team2 int,	battedfirst int,
    battedsecond int,	venue_name varchar(100) NOT NULL, city_name	varchar(100), country_name varchar(100), toss_winner int,
    match_winner	int, toss_name varchar(50),	win_type varchar(50), man_of_match int,  win_margin int, primary key (match_id),
    foreign key(team1) references TEAM(team_id), foreign key(team2) references TEAM(team_id), 
    foreign key(battedfirst) references TEAM(team_id), foreign key (battedsecond) references TEAM(team_id))''')

    cur.execute('''CREATE TABLE PLAYER_MATCH (playermatch_key int, match_id int,  player_id int, batting_hand varchar(50),
    bowling_skill varchar(50), role_desc varchar(50), team_id int, foreign key (match_id) references MATCH(match_id),
    foreign key (player_id) references PLAYER(player_id), foreign key (team_id) references TEAM(team_id), primary key (playermatch_key))''')

    cur.execute('''CREATE TABLE BALL_BY_BALL(match_id int,  innings_no	int, over_id int,  ball_id int, striker_batting_position int,  runs_scored int, 
    extra_runs	int, out_type varchar(50), striker int, non_striker	int, bowler int, primary key (match_id, innings_no, over_id, ball_id),foreign key (striker) references PLAYER(player_id),
    foreign key (non_striker) references PLAYER(player_id))''')

    ipl.commit()
    ipl.close()