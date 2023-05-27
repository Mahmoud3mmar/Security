import json
import socket
import csv

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('', 8000)  # '' means to listen on all available interfaces
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print(f'Server is listening on {server_address[0]}:{server_address[1]}')

# Wait for a connection
print('Waiting for a connection...')
client_socket, client_address = server_socket.accept()
print(f'Accepted connection from {client_address[0]}:{client_address[1]}')


def decrypt(ciphertext, d, n):
    # Convert d and n to integers
    d = int(d)
    n = int(n)

    # Decrypt the ciphertext
    plaintext = ''.join([chr(pow(c, d, n)) for c in ciphertext])

    return plaintext






# Loop to receive and send messages
while True:

    # import the module containing the DES class
    # import RSA
    # import CentralRepoServer
    # import PrivateKeysServer
    import CentralRepo
    import RSA
    CentralRepo.add_public_keys('Server', RSA.e1, RSA.n1)
    print( RSA.e1, RSA.n1)


    message = input('Client: ')
    # Receive data from the client
    data = client_socket.recv(1024)

    # If no data received, the client has closed the connection
    if not data:
        print(f'Connection closed by {client_address[0]}:{client_address[1]}')
        break

    # Decode the received bytes to string
    received_message = data


    # print(CentralRepoServer.get_public_keys('Kareem'))
    # print(PrivateKeysServer.get_private_keys('Kareem'))
    # decoded_string = received_message.decode('utf-8')  # decode the bytes as a string
    # decoded_values = json.loads(decoded_string)  # deserialize the string to a list of integers
    # #
    print('dec',received_message)
    # a,b=PrivateKeys.get_private_keys('Kareem')





    # decrypt=decrypt(decoded_values,a, b)

    print(f'Received encrypt message from before encode : {received_message}')

    # print(f'Received encrypt message from : {decoded_values}')
    print(f'Received decrypted message from : {decrypt}')



    # message_str = received_message.decode('utf-8')  # decode the bytes object to a string

    # print(f'Received Encrypted message from {client_address[0]}:{client_address[1]}: {received_message}')


    # create an instance of the DES class with a key of your choice (as bytes) for decryption
    # key = b'somekey12345678'
    # # key = TTP.run_ttpA()
    # des = DES(key)
    # ciphertext = received_message
    # decrypted_text = des.Decrypt(ciphertext)
    #
    # # Receive Encrypted message & Decrypt it
    # print(f'Received Encrypted message from {client_address[0]}:{client_address[1]}: {ciphertext}')
    # print(f'Received Decrypted message from {client_address[0]}:{client_address[1]}: {decrypted_text}')
    # # Get input from the server user
    message = input('Server: ')

    # create an instance of the DES class with a key of your choice (as bytes) for encryption
    # key = b'somekey12345678'
    # des = DES(key)
    # ciphertext = des.Encrypt(message.encode('utf-8'))
    # Send Encrypted data to the server
    client_socket.sendall(message.encode('utf-8'))

# Close the connection
client_socket.close()
