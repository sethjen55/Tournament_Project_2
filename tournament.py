#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname = tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    rs = conn.cursor()
    rs.execute("DELETE FROM tblMatches")
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    rs = conn.cursor()
    rs.execute("DELETE FROM tblPlayers")
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    rs = conn.cursor()
    rs.execute("SELECT COUNT(id) FROM tblPlayers;")
    rows = rs.fetchall()
    conn.close()
    return rows[0][0]

def registerPlayer(name):
    """Adds a player to the tournament database."""
    conn = connect()
    rs = conn.cursor()
    rs.execute("INSERT INTO tblPlayers (name) VALUES (%s)", (bleach.clean(name, strip=True),))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins."""
    conn = connect()
    rs = conn.cursor()
    rs.execute("SELECT id, name, wins, matches FROM vwStandings ORDER BY wins DESC;")
    rows = rs.fetchall()
    conn.close()
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players."""
    conn = connect()
    rs = conn.cursor()
    rs.execute("INSERT INTO tblMatches (winner, looser) VALUES (%s,%s)",(winner, loser))
    conn.commit()
    conn.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings."""
    
    conn = connect()
    rs = conn.cursor()
    rs.execute("SELECT id, name FROM vwWinCount ORDER BY wins DESC, id;")
    rows = rs.fetchall()
    conn.close()

    """ Takes the returned rows from the Win Count view and pairs up players """
    i=0
    pairings = []
    while i < len(rows):
        id1 = rows[i][0]
        name1 = rows[i][1]
        id2 = rows[i+1][0]
        name2 = rows[i+1][1]
        pairings.append((id1, name1, id2, name2))
        i=i+2

    return pairings


