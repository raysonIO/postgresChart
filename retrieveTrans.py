#Retreive data from database and transform for use in plotting
import psycopg2
			# leave host blank for local host
con = psycopg2.connect(
			host="",
			database="general",
			user="postgres",
			password="./anita"
			)
cur = con.cursor()
cur.execute(
		"SELECT cause, race, deaths from table_1;"
		""
		
		)
print(cur.fetchall())

#Close cursors and connections
con.commit()
cur.close()
con.close()



#Filter by diseases of the heart
#then filter by race
#Slices  = sum of deaths 