file_name = 'private_keysServer.txt'


# Initialize the text file
def initialize_text_file():
    with open(file_name, mode='w') as f:
        f.write('Identifier,PrivateKey1,PrivateKey2\n')


# Add private keys to the text file
def add_private_keys(identifier, private_key1, private_key2):
    with open(file_name, mode='a') as f:
        f.write(f'{identifier},{private_key1},{private_key2}\n')


# Retrieve private keys from the text file by identifier
def get_private_keys(identifier):
    with open(file_name, mode='r') as f:
        for line in f:
            line = line.strip()
            id, private_key1, private_key2 = line.split(',')
            if id == identifier:
                return private_key1, private_key2

    return None, None


# Update private keys in the text file by identifier
def update_private_keys(identifier, new_private_key1, new_private_key2):
    records = []

    with open(file_name, mode='r') as f:
        for line in f:
            records.append(line)

    with open(file_name, mode='w') as f:
        f.write('Identifier,PrivateKey1,PrivateKey2\n')  # Write header

        for record in records:
            id, private_key1, private_key2 = record.split(',')
            if id == identifier:
                f.write(f'{identifier},{new_private_key1},{new_private_key2}\n')
            else:
                f.write(record)


# Initialize the text file
initialize_text_file()

# # Add private keys (replace the example keys with real private keys)
# add_private_keys('user1', 'USER1_PRIVATE_KEY1_HERE', 'USER1_PRIVATE_KEY2_HERE')
# add_private_keys('user2', 'USER2_PRIVATE_KEY1_HERE', 'USER2_PRIVATE_KEY2_HERE')
#
# # Retrieve private keys
# private_key1, private_key2 = get_private_keys('user1')
# print(f"Private keys for user1: {private_key1}, {private_key2}")
#
# # Update private keys (replace the example keys with real private keys)
# update_private_keys('user1', 'USER1_NEW_PRIVATE_KEY1_HERE', 'USER1_NEW_PRIVATE_KEY2_HERE')

# Verify that the private keys have been updated
# private_key1, private_key2 = get_private_keys('user1')
# print(f"Updated private keys for user1: {private_key1}, {private_key2}")

