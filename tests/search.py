import json
import sys

from app.database.database import get_connection


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m tests.search \"item name\"")
        return

    search_text = sys.argv[1]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT endpoint, name, category, json_data
        FROM nexus_raw_data
        WHERE name LIKE ?
        ORDER BY endpoint, name
        LIMIT 20
    """, (f"%{search_text}%",))

    rows = cursor.fetchall()

    if not rows:
        print("No results found.")
        conn.close()
        return

    for endpoint, name, category, json_data in rows:
        data = json.loads(json_data)

        print("\n==============================")
        print(f"Endpoint: {endpoint}")
        print(f"Name: {name}")
        print(f"Category: {category}")

        properties = data.get("Properties") or {}
        economy = properties.get("Economy") or {}

        if economy:
            print("Economy:", economy)

        if "Damage" in properties:
            print("Damage:", properties["Damage"])

        if "Range" in properties:
            print("Range:", properties["Range"])

        if "UsesPerMinute" in properties:
            print("Uses/min:", properties["UsesPerMinute"])

        if "Skill" in properties:
            print("Skill:", properties["Skill"])

        if "ProfessionHit" in data:
            print("Profession Hit:", data["ProfessionHit"].get("Name"))

        if "ProfessionDmg" in data:
            print("Profession Dmg:", data["ProfessionDmg"].get("Name"))

    conn.close()


if __name__ == "__main__":
    main()