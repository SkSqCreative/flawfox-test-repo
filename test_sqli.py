# Test file for SQL Injection vulnerability
import sqlite3

def get_user(username):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Vulnerable line: SQL query built using string concatenation
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    print(f"Executing: {query}") # Debug print

    try:
        cursor.execute(query)
        user_data = cursor.fetchone()
        return user_data
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

# Example usage (DON'T run this with untrusted input!)
user_input = "admin' OR '1'='1" 
get_user(user_input)
