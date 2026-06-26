from app.database.database import get_connection

conn = get_connection()
cursor = conn.cursor()

print("\n=== Endpoint Counts ===")

cursor.execute("""
SELECT endpoint, COUNT(*)
FROM nexus_raw_data
GROUP BY endpoint
ORDER BY endpoint
""")

for row in cursor.fetchall():
    print(row)

print("\n=== Weapon Categories ===")

cursor.execute("""
SELECT category, COUNT(*)
FROM nexus_raw_data
WHERE endpoint = ?
GROUP BY category
ORDER BY COUNT(*) DESC
""", ("weapons",))

for row in cursor.fetchall():
    print(row)

conn.close()