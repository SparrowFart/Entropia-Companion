from .database import get_connection


def get_all_skills():
    # Gets all skills from the database, sorted by name
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, category, is_hidden
        FROM skills
        ORDER BY name
    """)

    skills = cursor.fetchall()

    connection.close()

    return skills