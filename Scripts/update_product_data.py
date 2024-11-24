import sqlite3
from database import ensure_connection
def add_product_into_category(conn, name, category, color, quantity, price):
    """Function to add a new product to the database."""
    conn = ensure_connection(conn)
    try:
        cursor = conn.cursor()
        
        # Debug: Print the values being inserted
        print(f"Attempting to add: Name={name}, Category={category}, Color={color}, Quantity={quantity}, Price={price}")
        
        # Insert product into the Products table
        cursor.execute("""
            INSERT INTO Products (Name, Category, Color, Quantity, Price)
            VALUES (?, ?, ?, ?, ?)
        """, (name, category, color, quantity, price))

        conn.commit()
        print(f"Product '{name}' added successfully!")
        conn.close()
    except sqlite3.Error as e:
        print(f"Error adding product: {e}")

def remove_product_by_id(conn, product_id):
    """Function to remove a product from the database by ProductID."""
    conn = ensure_connection(conn)
    try:
        cursor = conn.cursor()
        # Delete product by ProductID
        cursor.execute("DELETE FROM Products WHERE ProductID = ?", (product_id,))
        conn.commit()  # Commit the transaction
        print(f"Product with ProductID {product_id} removed successfully!")
        conn.close()
    except sqlite3.Error as e:
        print(f"Error removing product: {e}")

def update_quantity(conn, product_id, quantity):
    """
    Increment or decrement the quantity of an item.
    
    :param conn: The database connection object
    :param db_path: Path to the database
    :param product_id: The ID of the product to update
    :param amount: Positive value to increment, negative to decrement
    """
    
    conn = ensure_connection(conn)  # Ensure the connection is open
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Products
            SET Quantity = ?
            WHERE ProductID = ?;
        """, (quantity, product_id))
        conn.commit()
        print(f"Updated ProductID {product_id} to {quantity}.")
    except sqlite3.Error as e:
        print(f"Error updating quantity: {e}")

