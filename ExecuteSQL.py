#ONE TIME THING ONLY
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("PGUSER")
password = os.getenv("PGPASSWORD")
database = os.getenv("PGDATABASE")

os.environ["PGPASSWORD"] = password

subprocess.run(
    ["psql", "-U", user, "-d", "postgres", "-c", f"CREATE DATABASE {database};"],
    check=True
)
print("Database created successfully.")

subprocess.run(
    ["psql", "-U", user, "-d", database, "-f", "restaurants.sql"],
    check=True
)
print("SQL file executed successfully.")