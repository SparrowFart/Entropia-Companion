from datetime import datetime

from app.database.database import get_connection


CHARACTER_NAME = "Test Character"


def main():
    conn = get_connection()
    cursor = conn.cursor()

    now = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")

    cursor.execute("""
        INSERT OR REPLACE INTO characters
        (
            full_name,
            current_hp,
            total_skill_count,
            skills_last_updated
        )
        VALUES (?, ?, ?, ?)
    """, (
        CHARACTER_NAME,
        163,
        250000,
        now,
    ))

    cursor.execute("""
        SELECT id, full_name, current_hp, total_skill_count, skills_last_updated
        FROM characters
    """)

    for row in cursor.fetchall():
        print(row)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()