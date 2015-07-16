# Tournament_Project_2
Udacity Full Stack Web Developer Programming Assignment 2 - Python Tournament Results

##Files that are used in this Project
* tournament.py -- implementation of a Swiss-system tournament
* tournament.sql -- table definitions for the tournament project.
* tournament_test.py -- Test cases for tournament.py

##Functions in tournament.py
###registerPlayer(name)
Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

###countPlayers()
Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

###deletePlayers()
Clear out all the player records from the database.
reportMatch(winner, loser)
Stores the outcome of a single match between two players in the database.

###deleteMatches()
Clear out all the match records from the database.

###playerStandings()
Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

###swissPairings()
Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.

##Setup and usage of the files
* First, set up the tournament database if it doesn't already exist
From the psql console; use the create database
```bash
vagrant=> CREATE DATABASE tournament;
CREATE DATABASE
vagrant=> \q
```
* Next, connect to Tournament Database and import the SQL schema file
```bash
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql tournament
tournament=> \i tournament.sql 
tournament=> \q
```
* Final step, Run the test file
```bash
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py 
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```
