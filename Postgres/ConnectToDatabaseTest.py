import pg8000

# Connect to database

conn = pg8000.connect(user='postgres', password='postgres', database='postgres')

# Create cursor

cursor = conn.cursor()

# Select rows in table

cursor.execute("SELECT * FROM people_and_photos_per_country")
results = cursor.fetchall()