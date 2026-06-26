# Entropia Companion - Project State

## Current status
- Python 3.11 used.
- Virtual environment created: venv
- VS Code installed and configured.
- Python interpreter set to venv.
- SQLite database created: companion.db
- Database initializes successfully.
- Test skill seed system created.

## Current structure
- main.py
- companion.db
- app/database/database.py
- app/database/seed_data.py
- app/database/queries.py

## Current design decision
- App will be simple and fast.
- Main navigation: Dashboard, Skills, Planner, Import, More.
- Character header always visible.
- Planner supports:
  - Cheapest PED route
  - Fewest chips
  - Fastest gain
  - Compare all

## Next step
Create ROADMAP.md.