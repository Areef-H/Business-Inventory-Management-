import sqlite3

def connect_to_db(db_name):
    """Connect to the SQLite database."""
    conn = sqlite3.connect(db_name)
    return conn

def execute_sql_file(conn, sql_file):
    """Execute SQL commands from a file."""
    with open(sql_file, 'r') as file:
        sql_script = file.read()
    conn.executescript(sql_script)
    conn.commit()
    print(f"Executed {sql_file} successfully.")