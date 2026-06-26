"""
Synchronization Service

Generic Nexus mirror:
downloads Nexus endpoints and stores them by endpoint/category/name.
"""

import hashlib
import json
from datetime import datetime

from app.database.database import get_connection
from app.services.nexus_api import NexusAPI


class SyncService:
    """Handles full Nexus synchronization."""

    def __init__(self):
        self.api = NexusAPI()

        self.supported_endpoints = [
            "skills",
            "professions",
            "weapons"
        ]

    def full_sync(self):
        print("Starting full Nexus synchronization...")

        for endpoint in self.supported_endpoints:
            self.sync_endpoint(endpoint)

        print("Full Nexus synchronization complete.")

    def sync_endpoint(self, endpoint):
        print(f"Downloading {endpoint}...")

        records = self.api.get(endpoint)
        synced_at = datetime.utcnow().isoformat()

        connection = get_connection()
        cursor = connection.cursor()

        active_record_ids = set()

        for record in records:
            record_id = self.get_record_id(record)
            name = self.get_record_name(record)
            category = self.get_record_category(record)
            json_text = json.dumps(record, sort_keys=True)
            json_hash = hashlib.sha256(json_text.encode("utf-8")).hexdigest()

            active_record_ids.add(record_id)

            cursor.execute(
                """
                INSERT OR REPLACE INTO nexus_raw_data
                (
                    endpoint,
                    record_id,
                    name,
                    category,
                    json_data,
                    json_hash,
                    last_synced,
                    is_removed,
                    removed_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, 0, NULL)
                """,
                (
                    endpoint,
                    record_id,
                    name,
                    category,
                    json_text,
                    json_hash,
                    synced_at,
                ),
            )

        self.mark_removed_records(cursor, endpoint, active_record_ids, synced_at)

        connection.commit()
        connection.close()

        print(f"Stored {len(records)} active records from {endpoint}.")

    def mark_removed_records(self, cursor, endpoint, active_record_ids, synced_at):
        cursor.execute(
            """
            SELECT record_id
            FROM nexus_raw_data
            WHERE endpoint = ?
            AND is_removed = 0
            """,
            (endpoint,),
        )

        local_record_ids = {row[0] for row in cursor.fetchall()}
        removed_record_ids = local_record_ids - active_record_ids

        for record_id in removed_record_ids:
            cursor.execute(
                """
                UPDATE nexus_raw_data
                SET is_removed = 1,
                    removed_at = ?,
                    last_synced = ?
                WHERE endpoint = ?
                AND record_id = ?
                """,
                (synced_at, synced_at, endpoint, record_id),
            )

        if removed_record_ids:
            print(f"Marked {len(removed_record_ids)} removed records from {endpoint}.")

    def get_record_id(self, record):
        if "Id" in record:
            return str(record["Id"])

        if "ItemId" in record:
            return str(record["ItemId"])

        raise ValueError(f"Could not find record ID for record: {record}")

    def get_record_name(self, record):
        if "Name" in record:
            return record.get("Name")

        if "Item" in record and isinstance(record["Item"], dict):
            return record["Item"].get("Name")

        return None

    def get_record_category(self, record):
        category = record.get("Category")

        if isinstance(category, dict):
            return category.get("Name")

        if isinstance(category, str):
            return category

        properties = record.get("Properties")

        if isinstance(properties, dict):
            if "Category" in properties:
                return properties.get("Category")

        return None