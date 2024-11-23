from database import connect_to_db, execute_sql_file
from menu import menu
def main():
    # Step 1: Connect to the database
    conn = connect_to_db('Inventory_db/inventory.db')  # Adjust the path to your database
    print("Connected to the database.")

    # Step 2: Execute the schema creation script
    execute_sql_file(conn, 'Inventory_db/database.sql')  # Ensure the path matches your setup

    # Step 3: Execute the data insertion script
    execute_sql_file(conn, 'Inventory_db/insert_data.sql')

    # Close the connection
    
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    main()