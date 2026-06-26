"""
Database Report

Shows a summary of everything currently mirrored from Nexus.
"""

from app.database.database import get_connection


def main():
    connection = get_connection()
    cursor = connection.cursor()

    print("\n=== Nexus Database Report ===\n")

    cursor.execute("""
        SELECT endpoint, COUNT(*)
        FROM nexus_raw_data
        GROUP BY endpoint
        ORDER BY endpoint
    """)

    total = 0

    for endpoint, count in cursor.fetchall():
        print(f"{endpoint:<20} {count}")
        total += count

    print("\n----------------------------")
    print(f"TOTAL RECORDS: {total}")

    connection.close()


if __name__ == "__main__":
    main()