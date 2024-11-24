from database import connect_to_db, ensure_connection

class display_menu():

     def main_menu(self):
        print("----Options----")
        print("""
                1.) Add Products into a Category
                2.) Remove Products from a Category
                3.) Update Quantity of Products in Category
                4.) Display Products/Category Listings
                5.) Exit
                """)
     def category_menu(self):
        print("--Category Options--")
        print("""
                1.) Electronics
                2.) Accessories
                3.) Mechanical Parts
                4.) Software
             """)    
        return
           

     """ Utilizing SQLite """
     def display_product_listing(self,conn,table_name):
        """Fetch and display all rows from the specified table."""
        conn = ensure_connection(conn)
        cursor = conn.cursor()

        try:
            # Query to select all rows from the specified table
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()

            # Display the table headers
            print(f"\n--- {table_name.upper()} TABLE ---")
            column_names = [description[0] for description in cursor.description]
            print(" | ".join(column_names))  # Print column headers
            print("-" * 50)

            # Display each row
            for row in rows:
                print(" | ".join(map(str, row)))

        except Exception as e:
            print(f"Error fetching data from table {table_name}: {e}")
        finally:
            conn.close()
     


 
    

    