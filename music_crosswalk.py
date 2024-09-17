'''This project integrates Python and SQL. I will be creating and managing a database, building a schema, and performing various SQL operations including quiries with joins, filtes, and aggregations. '''

# Standard library imports
import sqlite3
import pathlib
import csv
import logging

# External library imports (requires virtual environment)
import pandas as pd

#Local module imports (if needed)

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

logging.info("Program started") # add this at the beginning of the main method
logging.info("Program ended")  # add this at the end of the main method

###############################
# File Paths
###############################

# Paths to the CSV files
artists_data_path = 'artists.csv'
songs_data_path = 'songs.csv'

# Database file path
db_file_path = 'music_database.db'


# Your code here....
# Define paths...
# Define functions...

# Define the main function that will call your functions
def main():
    paths_to_verify = [sql_file_path, artists_data_path, songs_data_path]
    verify_and_create_folders(paths_to_verify)
    
    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, artists_data_path, songs_data_path)









##############################
# Main function
##############################

def main():
    ...

    # Create database schema and populate with data
    ... your code here to perform all required operations


#####################################
# Conditional Execution
#####################################

# Conditionally execute the main() function if this is the script being run
if __name__ == "__main__":
    main()