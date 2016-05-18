import pg8000

# Connect to database

conn = pg8000.connect(user='postgres', password='postgres', database='thesisdb')

# Create cursor

cursor = conn.cursor()

# Select rows in table

cursor.execute("SELECT * FROM point_clusters_50_250")
results = cursor.fetchall()
assert isinstance(results, object)
for row in results:
    print row
