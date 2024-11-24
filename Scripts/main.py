from database import connect_to_db, execute_sql_file
from menu import menu
import sqlite3
def main():
    conn = connect_to_db('Inventory_db/inventory.db')  # Path to the database file

    # Step 2: Execute the schema creation script
    execute_sql_file(conn, 'Inventory_db/database.sql')  # Run table creation SQL

    # Step 3: Execute the data insertion script
    execute_sql_file(conn, 'Inventory_db/insert_data.sql')  # Run data insertion SQL

    menu().menu_main()
    
    conn.close()

if __name__ == "__main__":
    main()