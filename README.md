# Project 5 SQL Module
Project 5 integrates Python and SQL, focusing on database interactions using SQLite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

## Create and Activate Project Virtual Environment
py -m venv .venv
.venv\Scripts\Activate

## Add and Commit Changes to Github
git add . git commit -m git push -u origin main

## Add external dependencies
pip install pandas pip install pyarrow

## Create files
.gitignore  
README.md 
requirements.txt 
data folder with artits.csv  and songs.csv files with data
SQL folder with the following files:
create_tables.sql - with sql code to create your database schema using sql
insert_records.sql - with sql code to insert at least 10 additional records into each table.
update_records.sql - with sql code to update 1 or more records in a table.
delete_records.sql - with sql code to delete 1 or more records from a table.
query_aggregation.sql - with sql code to use aggregation functions including COUNT, AVG, SUM.
query_filter.sql - with sql code to use WHERE to filter data based on conditions.
query_sorting.sql - with sql code to use ORDER BY to sort data.
query_group_by.sql - with sql code to use GROUP BY clause (and optionally with aggregation)
query_join.sql - with sql code to use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.
music_crosswalk.py (for Python code to run sql commands)  
project.db (database file created using Python code)  

## Schema Design
### Schema Overview
This schema will have to tables:
1.  Artists:  Stores artists details.
2.  Songs:  Stores details about songs with references to the artist.

### Schema Description
Authors Table: Contains author_id (primary key), name, and birth_year.
Books Table: Contains book_id (primary key), title, publication_year, and author_id (foreign key).  

## Create Python Script to Create and Populate the Database
## Create SQL Operations
## Create Python Script to exececute SQL operations

