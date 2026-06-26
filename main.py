from app.database.database import initialize_database
from app.database.seed_data import seed_skills

print("Starting Entropia Companion...")

initialize_database()
seed_skills()

print("Database initialized successfully!")
print("Test skills added successfully!")