''' 
This code creates a table called browserhistory in a PostgreSQL database and populates it with up to 
10,000 entries extracted from a Chrome browser history JSON file.
'''

import psycopg2
import environ
import json

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='postgres',
    password=env('DBPASS'),
    database=env('DATABASE')
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the 'browserhistory' table if it doesn't exist
# The table has columns: id, title, url, and time_usec
cursor.execute('''
    CREATE TABLE IF NOT EXISTS browserhistory
    (id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    time_usec BIGINT NOT NULL)
''')

# Open and read the Chrome Browser History JSON file
# The file is expected to be in the directory 'Chrome' and named 'BrowserHistory.json'
with open('Chrome/BrowserHistory.json', 'r', encoding='utf-8') as f:
    # Load JSON data from file
    data = json.load(f)

# Extract the first 10000 entries from the 'Browser History' section of the loaded JSON data
data_list = data['Browser History'][0:10000]

# Insert the extracted data into the 'browserhistory' table
# Each entry consists of: title, url, and time_usec
for entry in data_list:
    cursor.execute("INSERT INTO browserhistory (title, url, time_usec) VALUES (%s, %s, %s)",
                   (entry['title'], entry['url'], entry['visitCount']))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
