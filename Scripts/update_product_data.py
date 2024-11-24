import sqlite3

def add_product_into_category(name, category, color, quantity, price):
    """Function to add a new product to the database."""
    try:
        conn = sqlite3.connect('../databases/inventory.db')  # Connect to the database
        cursor = conn.cursor()
        
        # Insert product into the Products table
        cursor.execute("""
            INSERT INTO Products (Name, Category, Color, Quantity, Price)
            VALUES (?, ?, ?, ?, ?)
        """, (name, category, color, quantity, price))

        conn.commit()
        print(f"Product '{name}' added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding product: {e}")
    finally:
        conn.close()



