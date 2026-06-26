"""
Nexus API client.

This file is responsible ONLY for talking to the Entropia Nexus API.
No UI code belongs here.
No database code belongs here.
"""

import requests


class NexusAPI:
    """Handles requests to the Entropia Nexus API."""

    def __init__(self):
        self.base_url = "https://api.entropianexus.com"

    def get(self, endpoint):
        """Download JSON data from one Nexus endpoint."""

        url = f"{self.base_url}/{endpoint}"

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        return response.json()