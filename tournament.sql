-- Table definitions for the tournament project.

\c tournament
DROP VIEW IF EXISTS vwStandings;
DROP View IF EXISTS vwMatchCount;
DROP VIEW IF EXISTS vwWinCount;
DROP VIEW IF EXISTS vwLossCount;
DROP TABLE IF EXISTS tblMatches;
DROP TABLE IF EXISTS tblPlayers;
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;
\c tournament

-- Players Table
CREATE TABLE tblPlayers (
	id SERIAL primary key,
	name varchar(50)
);

-- Matches Table
CREATE TABLE tblMatches (
	id SERIAL primary key,
	winner int references tblPlayers(id),
	looser int references tblPlayers(id)
);

-- Wins View shows number of wins for each Player
CREATE VIEW vwWinCount AS
	SELECT 
		P.id,
		P.name,
		COUNT(M.winner) AS wins 
	FROM 
		tblPlayers AS P
	LEFT JOIN tblMatches AS M
		ON P.id = M.winner
	GROUP BY 
		P.id,
		P.name
	ORDER BY 
		wins DESC;

-- Loss View shows number of losses for each Player
CREATE VIEW vwLossCount AS
	SELECT 
		P.id, 
		COUNT(M.looser) AS losses 
	FROM 
		tblPlayers AS P
	LEFT JOIN tblMatches AS M
		ON P.id = M.looser
	GROUP BY 
		P.id
	ORDER BY 
		losses DESC;

-- Count View shows number of matches for each Player
CREATE VIEW vwMatchCount AS
	SELECT 
		P.id, 
		(W.wins + L.losses) AS matches 
	FROM 
		tblPlayers AS P
		LEFT JOIN vwWinCount AS W
			ON P.id = W.id
		INNER JOIN vwLossCount AS L
			ON P.id = L.id
	ORDER BY 
		matches DESC;

-- Standings View shows number of wins and matches for each Player
CREATE VIEW vwStandings AS 
	SELECT 
		P.id, 
		P.name,
		W.wins,
		M.matches 
	FROM 
		tblPlayers AS P
		INNER JOIN vwWinCount AS W
			ON P.id = W.id
		INNER JOIN vwMatchCount AS M
			ON W.id = M.id;

		