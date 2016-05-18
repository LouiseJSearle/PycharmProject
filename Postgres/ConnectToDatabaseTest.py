import pg8000

# Connect to database

conn = pg8000.connect(user='postgres', password='postgres', database='postgres')
cursor = conn.cursor()
cursor.execute("SELECT * FROM people_and_photos_per_country")
results = cursor.fetchall()