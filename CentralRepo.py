import sqlite3

with sqlite3.connect('keys.db') as connection:
    cursor = connection.cursor()

    # Create a table to store public keys
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS public_keys (
        id INTEGER PRIMARY KEY,  
        identifier VARCHAR(255) NOT NULL UNIQUE,
        public_key1 VARCHAR(255) NOT NULL,
        public_key2 VARCHAR(255) NOT NULL
    )
    """)

    # Add public keys to the table
    def add_public_keys(identifier, public_key1, public_key2):
        cursor.execute("""
        INSERT INTO public_keys (identifier, public_key1, public_key2)
        VALUES (?, ?, ?)
        """, (identifier, public_key1, public_key2))

    # Retrieve public keys from the table by identifier
    def get_public_keys(identifier):
        cursor.execute("SELECT public_key1, public_key2 FROM public_keys WHERE identifier=?", (identifier,))
        return cursor.fetchone()

    # Update public keys in the table by identifier
    def update_public_keys(identifier, new_public_key1, new_public_key2):
        cursor.execute("""
        UPDATE public_keys
        SET public_key1=?, public_key2=? 
        WHERE identifier=?
        """, (new_public_key1, new_public_key2, identifier))

    # # Example usage
    # add_public_keys('user1', 'USER1_PUBLIC_KEY1_HERE', 'USER1_PUBLIC_KEY2_HERE')
    # public_key1, public_key2 = get_public_keys('user1')
    # print(f"Public keys for user1: {public_key1}, {public_key2}")
    #
    # update_public_keys('user1', 'USER1_NEW_PUBLIC_KEY1_HERE', 'USER1_NEW_PUBLIC_KEY2_HERE')
    # public_key1, public_key2 = get_public_keys('user1')
    # print(f"Updated public keys for user1: {public_key1}, {public_key2}")