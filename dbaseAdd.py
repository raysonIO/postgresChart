import psycopg2
			# leave host blank for local host
con = psycopg2.connect(
			host="",
			database="general",
			user="postgres",
			password="./anita"
			)
cur = con.cursor()
cur.execute("ALTER TABLE TABLE_1 " 
			"ADD SEX CHAR(1), "
			"ADD RACE VARCHAR(30), "
			"ADD DEATHS TEXT, "
			"ADD DEATH_RATE TEXT, "
			"ADD AADJ_DATE TEXT")

#Close cursors and connections
con.commit()
cur.close()
con.close()

#show tables with psql -> \c name of database

# add rows to database with python

 