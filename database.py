# NOT SURE WHY WE NEED TO DELETE THE TABLES AND THEN CREATE THEM AGAIN
import sqlite3 as lite

con = lite.connect('getting_startedv2.db')

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities;")
    cur.execute("DROP TABLE IF EXISTS weather;")
    cur.execute("CREATE TABLE cities (name text, state text);")
    cur.execute("CREATE TABLE weather (City text, Year integer, Warm_Month text, Cold_Month text, Average_High integer);")
	
# NOT SURE IF IMPORTING "sqlite3 as lite" IS REQUIRED AGAIN OR IF IT IS REDUNDANT
import sqlite3 as lite

cities = (('New York', 'NY'),
          ('Boston', 'MA'),
          ('Chicago', 'IL'),
          ('Miami', 'FL'),
          ('Dallas', 'TX'),
          ('Seattle', 'WA'),
          ('Portland', 'OR'),
          ('San Francisco', 'CA'),
          ('Los Angeles', 'CA'),
          ('Las Vegas', 'NV'),
          ('Atlanta', 'GA'))

weather = (('New York', 2013, 'July', 'January', 62),
          ('Boston', 2013, 'July', 'January', 59),
          ('Chicago', 2013, 'July', 'January', 59),
          ('Miami', 2013, 'August', 'January', 84),
          ('Dallas', 2013, 'July', 'January', 77),
          ('Seattle', 2013, 'July', 'January', 61),
          ('Portland', 2013, 'July', 'December', 63),
          ('San Francisco', 2013, 'September', 'December', 64),
          ('Los Angeles', 2013, 'September', 'December', 75),
          ('Las Vegas', 2013, 'July', 'December', 80),
          ('Atlanta', 2013, 'July', 'January', 80))

con = lite.connect('getting_startedv2.db')

with con:

    cur = con.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
	
# NOT SURE IF IMPORTING "sqlite3 as lite" IS REQUIRED AGAIN OR IF IT IS REDUNDANT
import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_startedv2.db')

with con:

  cur = con.cursor()
  cur.execute("SELECT Warm_Month, name, state FROM weather INNER JOIN cities ON city = name GROUP BY name HAVING Warm_Month = 'July';")

  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows, columns=cols)
  
  print "The cities that are warmest in July are:"
  
  for row in rows:
    print row[1],",",row[2]