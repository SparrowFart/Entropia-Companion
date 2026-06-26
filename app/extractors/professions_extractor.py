"""
Professions Extractor

Reads raw profession data from nexus_raw_data
and populates relational profession tables.
"""

import json

from app.database.database import get_connection


class ProfessionsExtractor:
    """Extracts professions from raw Nexus data."""

    def run(self):
        print("Extracting professions...")

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                record_id,
                json_data,
                is_removed
            FROM nexus_raw_data
            WHERE endpoint = 'professions'
        """)

        rows = cursor.fetchall()

        for record_id, json_data, is_removed in rows:
            profession = json.loads(json_data)

            category = profession.get("Category") or {}

            cursor.execute(
                """
                INSERT OR REPLACE INTO professions
                (
                    id,
                    name,
                    category,
                    is_removed
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    int(record_id),
                    profession.get("Name"),
                    category.get("Name"),
                    is_removed,
                ),
            )

            self.extract_profession_skills(cursor, int(record_id), profession, is_removed)

        connection.commit()
        connection.close()

        print(f"Extracted {len(rows)} professions.")

    def extract_profession_skills(self, cursor, profession_id, profession, is_removed):
        """Extracts skill weight links for one profession."""

        skills = profession.get("Skills") or []

        for skill_link in skills:
            skill = skill_link.get("Skill") or {}
            links = skill.get("Links") or {}

            skill_id = self.get_id_from_url(links.get("$Url"))
            skill_name = skill.get("Name")
            weight = skill_link.get("Weight")

            if skill_id is None:
                continue

            cursor.execute(
                """
                INSERT OR REPLACE INTO profession_skills
                (
                    profession_id,
                    skill_id,
                    skill_name,
                    weight,
                    is_removed
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    profession_id,
                    skill_id,
                    skill_name,
                    weight,
                    is_removed,
                ),
            )

    def get_id_from_url(self, url):
        """Extracts the numeric ID from a Nexus URL like /skills/123."""

        if not url:
            return None

        return int(url.rstrip("/").split("/")[-1])