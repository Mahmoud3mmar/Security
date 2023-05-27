
import socket

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

# Loop to receive and send messages
while True:

    # import the module containing the DES class
    from DES import DES
    from ttp import TTP
    # import RSA
    # create an instance of the DES class with a key of your choice (as bytes)
    # key = b'somekey12345678'
    # des = DES(key)
    #
    # # encrypt a plaintext message (as bytes)
    # plaintext = b'this is a secret message'
    # ciphertext = des.Encrypt(plaintext)
    #
    # # decrypt the ciphertext to get the original plaintext back
    # decrypted_text = des.Decrypt(ciphertext)
    # # print(ciphertext)

    # Receive data from the client
    data = client_socket.recv(1024)

    # If no data received, the client has closed the connection
    if not data:
        print(f'Connection closed by {client_address[0]}:{client_address[1]}')
        break

    # Decode the received bytes to string
    received_message = data

    # create an instance of the DES class with a key of your choice (as bytes) for decryption
    key = b'somekey12345678'
    # key = TTP.run_ttpA()
    des = DES(key)
    ciphertext = received_message
    decrypted_text = des.Decrypt(ciphertext)

    # Receive Encrypted message & Decrypt it
    print(f'Received Encrypted message from {client_address[0]}:{client_address[1]}: {ciphertext}')
    print(f'Received Decrypted message from {client_address[0]}:{client_address[1]}: {decrypted_text}')
    # Get input from the server user
    message = input('Server: ')

    # create an instance of the DES class with a key of your choice (as bytes) for encryption
    key = b'somekey12345678'
    des = DES(key)
    ciphertext = des.Encrypt(message.encode('utf-8'))
    # Send Encrypted data to the server
    client_socket.sendall(ciphertext)

# Close the connection
client_socket.close()
