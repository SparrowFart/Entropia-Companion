"""
Generate Nexus endpoint list.

Reads the embedded OpenAPI data from the Nexus Swagger UI init file,
then writes plain GET collection endpoints into app/services/nexus_endpoints.py.

Rules:
- Include GET endpoints.
- Exclude paths with {parameters}.
- Exclude endpoints with required query parameters.
"""

import json
import re
import requests


INIT_URL = "https://api.entropianexus.com/docs/swagger-ui-init.js"
OUTPUT_FILE = "app/services/nexus_endpoints.py"


def main():
    print("Downloading Nexus Swagger init file...")

    response = requests.get(INIT_URL, timeout=30)
    response.raise_for_status()

    text = response.text

    match = re.search(
        r'"swaggerDoc"\s*:\s*(\{.*?\})\s*,\s*"customOptions"',
        text,
        re.DOTALL,
    )

    if not match:
        raise RuntimeError("Could not find swaggerDoc in Swagger init file.")

    swagger_doc = json.loads(match.group(1))
    paths = swagger_doc.get("paths", {})

    endpoints = []

    for path, methods in paths.items():
        if "{" in path or "}" in path:
            continue

        get_method = methods.get("get")

        if not get_method:
            continue

        parameters = get_method.get("parameters") or []

        has_required_query_parameter = False

        for parameter in parameters:
            if parameter.get("in") == "query" and parameter.get("required") is True:
                has_required_query_parameter = True
                break

        if has_required_query_parameter:
            continue

        endpoint = path.strip("/")

        if endpoint:
            endpoints.append(endpoint)

    endpoints = sorted(set(endpoints))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write("ENDPOINTS = [\n")

        for endpoint in endpoints:
            file.write(f'    "{endpoint}",\n')

        file.write("]\n")

    print(f"Generated {len(endpoints)} endpoints.")
    print(f"Updated {OUTPUT_FILE}")


if __name__ == "__main__":
    main()