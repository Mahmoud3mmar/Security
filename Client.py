







import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('192.168.100.9', 8000)
client_socket.connect(server_address)

while True:

    # import the module containing the DES class
    from DES import DES
    # import the module containing the ttp class
    from ttp import TTP

    # key_size = 10
    # ttp = TTP(key_size)
    # ttp.run_ttp()

    # create an instance of the DES class with a key of your choice (as bytes)
    # key = b'somekey12345678'
    # des = DES(key)

    # encrypt a plaintext message (as bytes)
    # plaintext = b'this is a secret message'
    # ciphertext = des.Encrypt(plaintext)

    # decrypt the ciphertext to get the original plaintext back
    # decrypted_text = des.Decrypt(ciphertext)
    # print(ciphertext)

    # Get input from the client user
    message = input('Client: ')


    # create an instance of the DES class with a key of your choice (as bytes)
    key = b'somekey12345678'
    # key = TTP.run_ttpA()

    des = DES(key)
    ciphertext =des.Encrypt(message.encode('utf-8'))
    #
    hex_values = ciphertext
    binary_values = ''.join(format(byte, '08b') for byte in hex_values)
    print(binary_values)

    # Send Encrypted data to the server
    client_socket.sendall(ciphertext)

    # Receive a response from the server
    data = client_socket.recv(1024)
    if not data:
        print('Connection closed by server')
        break
    # 1001111100011011000000100011001110111000000100001111101101101101
    # 0110000000011111011011111101001010011111111001100110110011100010
    received_message = data

    # create an instance of the DES class with a key of your choice (as bytes) for decryption

    key = b'somekey12345678'
    des = DES(key)
    ciphertext = received_message
    decrypted_text = des.Decrypt(ciphertext)
    print('Received Encrypted message from :',ciphertext)
    print('Received Decrypted message from :',decrypted_text)

# Close the connection
client_socket.close()