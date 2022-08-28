DROP TABLE players;
CREATE TABLE players (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(20) DEFAULT NULL,
  age int DEFAULT NULL,
  team varchar(20) DEFAULT NULL,
  type varchar(15) DEFAULT NULL,
  PRIMARY KEY (id)
)



DROP TABLE teams;
create table teams(
  id int NOT NULL AUTO_INCREMENT,
  tname varchar(20) DEFAULT NULL,
  hcity varchar(20) DEFAULT NULL,
   win int DEFAULT NULL,
  total_matches int DEFAULT NULL,
  PRIMARY KEY (id)
)

select p.name, p.type, t.tname, t.hcity from players p inner join teams t on p.team=t.tname;