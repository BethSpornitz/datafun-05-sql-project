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
create_tables_sql_file_path = pathlib.Path('sql') / 'create_tables.sql'
insert_new_records_sql_path = pathlib.Path('sql') / 'insert_new_records.sql'
delete_records_sql_path = pathlib.Path('sql') / 'delete_records.sql'
query_aggregation_sql_path = pathlib.Path('sql') / 'query_aggregation.sql'
query_filter_sql_path = pathlib.Path('sql') / 'query_filter.sql'
query_group_by_sql_path = pathlib.Path('sql') / 'query_group_by.sql'
query_join_sql_path = pathlib.Path('sql') / 'query_join.sql'
query_sorting_sql_path = pathlib.Path('sql') / 'query_sorting.sql'
update_records_sql_path = pathlib.Path('sql') / 'update_records.sql'


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

def create_tables(db_file_path, create_tables_sql_file_path):
    """Read and execute SQL statements to create tables."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(create_tables_sql_file_path, "r") as file:
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

def insert_new_records(db_file_path):
    """Insert new records into the database."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(insert_new_records_sql_path, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Inserted new records from {insert_new_records_sql_path}")
    except sqlite3.Error as e:
        logging.exception(f"Error inserting new records: {e}")

def delete_records(db_file_path):
    """Delete records from the database."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(delete_records_sql_path, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Deleted records using {delete_records_sql_path}")
    except sqlite3.Error as e:
        logging.exception(f"Error deleting records: {e}")

def query_aggregation(db_file_path):
    """Perform aggregation queries."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(query_aggregation_sql_path, 'r') as file:
                sql_script = file.read()
            results = conn.execute(sql_script).fetchall()
            print("Aggregation query results:")
            for row in results:
                print(row)
            conn.executescript(sql_script)
            logging.info(f"Executed aggregation queries from {query_aggregation_sql_path}")
    except sqlite3.Error as e:
        logging.exception(f"Error executing aggregation queries: {e}")

def query_filter(db_file_path):
    """Perform filtered queries."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(query_filter_sql_path, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed filtered queries from {query_filter_sql_path}")
    except sqlite3.Error as e:
        logging.exception(f"Error executing filtered queries: {e}")

def query_group_by(db_file_path):
    """Perform queries with GROUP BY clause."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(query_group_by_sql_path, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed GROUP BY queries from {query_group_by_sql_path}")
    except sqlite3.Error as e:
        logging.exception(f"Error executing GROUP BY queries: {e}")

def query_join(db_file_path):
    """Perform queries with JOIN operations."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(query_join_sql_path, 'r') as file:
                sql_script = file.read()
            results = conn.execute(sql_script).fetchall()
            logging.info(f"Executed JOIN queries from {query_join_sql_path}")
            print("JOIN query results:")
            for row in results:
                print(row)
    except sqlite3.Error as e:
        logging.exception("Error executing JOIN queries")
        print(f"Error executing JOIN queries: {e}")

def query_sorting(db_file_path):
    """Perform sorting queries."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(query_sorting_sql_path, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed sorting queries from {query_sorting_sql_path}")
    except sqlite3.Error as e:
        logging.exception(f"Error executing sorting queries: {e}")

def update_records(db_file_path):
    """Update records in the database."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(update_records_sql_path, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Updated records using {update_records_sql_path}")
    except sqlite3.Error as e:
        logging.exception(f"Error updating records: {e}")

#####################################
#Define Main Function to call functions
#####################################

def main():

    logging.info("Program started") # add this at the beginning of the main method

    paths_to_verify = [
        pathlib.Path('sql') / 'create_tables.sql', 
        pathlib.Path('sql') / 'insert_new_records.sql',
        pathlib.Path('sql') / 'delete_records.sql',
        pathlib.Path('sql') / 'query_aggregation.sql',
        pathlib.Path('sql') / 'query_filter.sql',
        pathlib.Path('sql') / 'query_group_by.sql',
        pathlib.Path('sql') / 'query_join.sql',
        pathlib.Path('sql') / 'query_sorting.sql',
        pathlib.Path('sql') / 'update_records.sql',
        pathlib.Path('data') / 'artists.csv', 
        pathlib.Path('data') / 'songs.csv']
    
    verify_and_create_folders(paths_to_verify)

    create_database(db_file_path)
    create_tables(db_file_path, create_tables_sql_file_path)
    insert_data_from_csv(db_file_path, artists_data_path, songs_data_path)
    insert_new_records(db_file_path)
    delete_records(db_file_path)
    query_aggregation(db_file_path)
    query_filter(db_file_path)
    query_group_by(db_file_path)
    query_join(db_file_path)
    query_sorting(db_file_path)
    update_records(db_file_path)

    logging.info("Program ended")  # add this at the end of the main method

#####################################
# Conditional Execution
#####################################

# Conditionally execute the main() function if this is the script being run
if __name__ == "__main__":
    main()