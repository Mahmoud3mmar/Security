

import random

def get_prime(n):
    while True:
        num = random.randint(2 ** (n - 1), 2 ** n)
        if is_prime(num):
            return num

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def get_pq():
    p = get_prime(10)
    q = get_prime(10)
    return p, q

def get_ed(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    d = modinv(e, phi)
    if d is None:
        return None, None
    return e, d

def modinv(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return None

while True:
    p1, q1 = get_pq()
    n1 = p1 * q1
    e1, d1 = get_ed(p1, q1)

    if e1 is None or d1 is None:
        print("Key generation failed. Retrying...")
    else:
        break

print(f"Public key: ({e1}, {n1})")
print(f"Private key: ({d1}, {n1})")


def encrypt(plaintext, e, n):
    # Convert e and n to integers
    e = int(e)
    n = int(n)

    # Encrypt the plaintext
    ciphertext = [pow(ord(c), e, n) for c in plaintext]

    return ciphertext

def decrypt(ciphertext, d, n):
    # Convert d and n to integers
    d = int(d)
    n = int(n)

    # Decrypt the ciphertext
    plaintext = ''.join([chr(pow(c, d, n)) for c in ciphertext])

    return plaintext


#  # self.p, self.q = 97,29
# # #         # self.n = self.p * self.q
# # #         # self.e, self.d = 19,283
# cip=encrypt("hii",e1,n1)
# plain=decrypt(cip, d1,n1)
#
# print(cip)
# print(plain)