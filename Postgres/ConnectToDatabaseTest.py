import pg8000

# Connect to database

conn = pg8000.connect(user='postgres', password='postgres', database='thesisdb')
cursor = conn.cursor()