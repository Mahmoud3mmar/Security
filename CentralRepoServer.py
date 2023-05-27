file_name = 'public_keysServer.txt'


# Initialize the text file
def initialize_text_file():
    with open(file_name, mode='w') as f:
        f.write('Identifier,PublicKey1,PublicKey2\n')


# Add public keys to the text file
def add_public_keys(identifier, public_key1, public_key2):
    with open(file_name, mode='a') as f:
        f.write(f'{identifier},{public_key1},{public_key2}\n')


# Retrieve public keys from the text file by identifier
def get_public_keys(identifier):
    with open(file_name, mode='r') as f:
        for line in f:
            line = line.strip()
            id, public_key1, public_key2 = line.split(',')
            if id == identifier:
                return public_key1, public_key2

    return None, None


# Update public keys in the text file by identifier
def update_public_keys(identifier, new_public_key1, new_public_key2):
    records = []

    with open(file_name, mode='r') as f:
        for line in f:
            records.append(line)

    with open(file_name, mode='w') as f:
        f.write('Identifier,PublicKey1,PublicKey2\n')  # Write header

        for record in records:
            id, public_key1, public_key2 = record.split(',')
            if id == identifier:
                f.write(f'{identifier},{new_public_key1},{new_public_key2}\n')
            else:
                f.write(record)


# Initialize the text file
initialize_text_file()

# # Add public keys (replace the example keys with real public keys)
# add_public_keys('user1', 'USER1_PUBLIC_KEY1_HERE', 'USER1_PUBLIC_KEY2_HERE')
# add_public_keys('user2', 'USER2_PUBLIC_KEY1_HERE', 'USER2_PUBLIC_KEY2_HERE')
#
# # Retrieve public keys
# public_key1, public_key2 = get_public_keys('user1')
# print(f"Public keys for user1: {public_key1}, {public_key2}")
#
# # Update public keys (replace the example keys with real public keys)
# update_public_keys('user1', 'USER1_NEW_PUBLIC_KEY1_HERE', 'USER1_NEW_PUBLIC_KEY2_HERE')
#
# # Verify that the public keys have been updated
# public_key1, public_key2 = get_public_keys('user1')
# print(f"Updated public keys for user1: {public_key1}, {public_key2}")

# add_public_keys('Kareem',2,3)
#     # PrivateKeys.add_private_keys('Kareem', RSA.d1, RSA.n1)
# import RSA
# import PrivateKeysServer
# print(f"Public key 1: {RSA.e1} {RSA.n1}")
# print(f"Private key 1: {RSA.d1} {RSA.n1}")
# add_public_keys('Kareem', RSA.e1, RSA.n1)
# PrivateKeysServer.add_private_keys('Kareem', RSA.d1, RSA.n1)