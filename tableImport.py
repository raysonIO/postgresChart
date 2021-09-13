
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
		"COPY table_1(Year,Cause,Sex,Race,Deaths,Death_Rate,aadj_date)"
		"FROM 'C:\\Users\\Zephyr\\Raw Data\\New_York_City_Leading_Causes_of_Death.csv' "
		"DELIMITER ',' "
		"CSV HEADER;")

#Close cursors and connections
con.commit()
cur.close()
con.close()


#Ensure the columns in the "copy table" match the database columns exactly
