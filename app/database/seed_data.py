from .database import get_connection


def seed_skills():
    connection = get_connection()
    cursor = connection.cursor()

    skills = [
        ("Anatomy", "Medical", 0),
        ("Athletics", "General", 0),
        ("Combat Reflexes", "Combat", 0),
        ("Courage", "Combat", 0),
        ("Dexterity", "Attribute", 0),
        ("Evade", "Defense", 0),
        ("Serendipity", "Hidden", 1),
        ("Coolness", "Hidden", 1),
        ("Combat Sense", "Hidden", 1),
        ("Commando", "Hidden", 1),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO skills
        (name, category, is_hidden)
        VALUES (?, ?, ?)
    """, skills)

    connection.commit()
    connection.close()