import psycopg2
			# leave host blank for local host
con = psycopg2.connect(
			host="",
			database="general",
			user="postgres",
			password="./anita"
			)
cur = con.cursor()
cur.execute("Select * from pg_database;")

rows =cur.fetchall()
con.close()