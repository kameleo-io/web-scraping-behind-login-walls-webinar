import sqlite3


def init_profile_store(db_path='ip_profiles.db'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profiles (
            ip TEXT PRIMARY KEY,
            file_name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        REPLACE INTO profiles (ip, file_name) VALUES ('89.12.44.134', 'obi1keno2@gmail.com')
    ''')
    cursor.execute('''
        REPLACE INTO profiles (ip, file_name) VALUES ('89.12.44.135', 'DicksonAmanda@mail.com')
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()


def lookup_profile_by_ip(ip, db_path='ip_profiles.db'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)  # Ensure the database name matches your setup
    cursor = conn.cursor()

    # Execute SQL query to find the file name by IP address
    cursor.execute("SELECT file_name FROM profiles WHERE ip = ?", (ip,))
    result = cursor.fetchone()

    # Return the file name if the IP is found, else return None
    return result[0] if result else None


def insert_profile_by_ip(ip, file_name, db_path='ip_profiles.db'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Update or insert file_name by IP
    cursor.execute('''
        INSERT INTO profiles (ip, file_name) VALUES (?, ?)
        ON CONFLICT(ip) DO UPDATE SET file_name = excluded.file_name;
    ''', (ip, file_name))

    # Commit changes and close the connection
    conn.commit()
    conn.close()