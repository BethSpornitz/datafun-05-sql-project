'''This project integrates Python and SQL. I will be creating and managing a database, building a schema, and performing various SQL operations including quiries with joins, filtes, and aggregations. '''

# Standard library imports
import sqlite3
import pathlib
import logging

# External library imports (requires virtual environment)
import pandas as pd

###############################
#Logging
###############################
# 1. Configure logging to write to a file named log.txt.
# 2. Log the start of the program using logging.info().
# 3. Log the end of the program using logging.info().
# 4. Log exceptions using logging.exception().
# 5. Log other major events using logging.info().
# 6. Log the start and end of major functions using logging.debug().

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

###############################
# File Paths
###############################

# Paths to the CSV files
artists_data_path = pathlib.Path('data') / 'artists.csv'
songs_data_path = pathlib.Path('data') / 'songs.csv'

# Database file path
db_file_path = pathlib.Path('music_database.db')

#SQL file path
sql_file_path = pathlib.Path('sql') / 'create_tables.sql'


###############################
# Define Functions
###############################


def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
        else:
            print(f"Folder already exists: {folder}")

def create_database(db_file_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_file_path)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")

def create_tables(db_file_path, sql_file_path):
    """Read and execute SQL statements to create tables."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def insert_data_from_csv(db_file_path, artists_data_path, songs_data_path):
    """Read data from CSV files and insert the records into their respective tables."""
    try:
        #Verify that the CSV files exist and are not empty
        if not artists_data_path.exists():
            raise FileNotFoundError(f"{artists_data_path} does not exist")
        if not songs_data_path.exists():
            raise FileNotFoundError(f"{songs_data_path} does not exist")

        artists_df = pd.read_csv(artists_data_path)
        songs_df = pd.read_csv(songs_data_path)

        print(f"Artists DataFrame:\n{artists_df.head()}")
        print(f"Songs DataFrame:\n{songs_df.head()}")

        with sqlite3.connect(db_file_path) as conn:
            artists_df.to_sql("artists", conn, if_exists="replace", index=False)
            songs_df.to_sql("songs", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")

def main():

    logging.info("Program started") # add this at the beginning of the main method

    paths_to_verify = [sql_file_path, artists_data_path, songs_data_path]
    verify_and_create_folders(paths_to_verify)

    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, artists_data_path, songs_data_path)

    logging.info("Program ended")  # add this at the end of the main method

#####################################
# Conditional Execution
#####################################

# Conditionally execute the main() function if this is the script being run
if __name__ == "__main__":
    main()