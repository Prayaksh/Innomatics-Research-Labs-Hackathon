Innomatics Research Labs | Advanced GenAI Internship | Entrance Test
Project Overview
This repository contains the solution for the Innomatics Research Labs Advanced GenAI Internship Entrance Test. The objective was to construct a robust data pipeline that ingests, processes, and merges data from three distinct formats—JSON, SQL, and CSV—to create a unified dataset for analysis.

The final output is a consolidated dataset final_food_delivery_dataset.csv, which was used to derive insights and answer specific analytical questions provided in the assessment.

Repository Structure
ExecuteSQL.py: A utility script that handles database operations. It loads environment variables, connects to the PostgreSQL instance, executes the SQL dump, and extracts data into a DataFrame.

Restaurent.ipynb: The core logic file that:

Ingests raw JSON and CSV files.

Integrates the SQL data via ExecuteSQL.py.

Merges all three sources into a single DataFrame.

Performs data analysis to calculate the required metrics.

final_food_delivery_dataset.csv: The cleaned and merged final dataset.

.env.example: A template file containing the required environment variable keys for database connection.

Tech Stack
Language: Python

Data Manipulation: Pandas, NumPy

Database: PostgreSQL

Utilities: python-dotenv (for secure credential management), psycopg2

Methodology

1. Data Ingestion & Transformation
   The project required handling heterogeneous data sources:

SQL Integration: Instead of manually exporting CSVs, I wrote a Python script (ExecuteSQL.py) to automate the connection to PostgreSQL. It uses dotenv to safely load credentials, runs the raw SQL file to set up the environment, and queries the table directly into a DataFrame.

File Parsing: Parsed semi-structured JSON data and structured CSV data into compatible DataFrames.

2. Data Merging
   Identified common keys across the three datasets.

Performed merges to create a comprehensive view of the food delivery data, ensuring no critical data points were lost during the join process.

3. Analysis
   The final_food_delivery_dataset.csv was used to query specific metrics (e.g., delivery times, order values, customer demographics) as required by the entrance test questions.

How to Run Locally
Clone the Repository

Bash
git clone https://github.com/Prayaksh/Innomatics-Research-Labs-Hackathon.git
cd Innomatics-Research-Labs-Hackathon
Install Dependencies

Bash
pip install pandas psycopg2-binary python-dotenv
Environment Setup

Create a .env file by copying the provided example:

Bash
cp .env.example .env
Open .env and fill in your local PostgreSQL credentials (HOST, PORT, USER, PASSWORD, DB_NAME).

Execute the Pipeline Run the main script to generate the dataset and view the analysis results.
