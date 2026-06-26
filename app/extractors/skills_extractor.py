"""
Skills Extractor

Reads raw skill data from nexus_raw_data
and populates the relational skills table.
"""

import json

from app.database.database import get_connection


class SkillsExtractor:
    """Extracts skills from raw Nexus data."""

    def run(self):
        print("Extracting skills...")

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                record_id,
                json_data,
                is_removed
            FROM nexus_raw_data
            WHERE endpoint = 'skills'
        """)

        rows = cursor.fetchall()

        for record_id, json_data, is_removed in rows:

            skill = json.loads(json_data)

            properties = skill.get("Properties") or {}
            category = skill.get("Category") or {}

            cursor.execute(
                """
                INSERT OR REPLACE INTO skills
                (
                    id,
                    name,
                    category,
                    is_hidden,
                    is_extractable,
                    hp_increase,
                    is_removed
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    int(record_id),
                    skill.get("Name"),
                    category.get("Name"),
                    1 if properties.get("IsHidden") else 0,
                    1 if properties.get("IsExtractable") else 0,
                    properties.get("HpIncrease") or 0,
                    is_removed,
                ),
            )

        connection.commit()
        connection.close()

        print(f"Extracted {len(rows)} skills.")