import json

from app.database.database import get_connection


SEARCH_NAME = "ArMatrix BC-10 (L)"


conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
    SELECT endpoint, name, category, json_data
    FROM nexus_raw_data
    WHERE name LIKE ?
    LIMIT 5
""", (f"%{SEARCH_NAME}%",))

rows = cursor.fetchall()

for endpoint, name, category, json_data in rows:
    print("\n====================")
    print(endpoint)
    print(name)
    print(category)

    data = json.loads(json_data)
    print(json.dumps(data, indent=2))

conn.close()