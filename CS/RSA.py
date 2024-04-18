import random
import math
import time

def generate_rsa_keys(bit_length=16):
    
    p = generate_prime_number(bit_length // 2)
    q = generate_prime_number(bit_length // 2)
    n = p * q
    eul = (p - 1) * (q - 1)
    e = choose_public_exponent(eul)
    d = modular_inverse(e, eul)

    public_key = (n, e)
    private_key = (n, d)
    
    return public_key, private_key

def generate_prime_number(bit_length):
    while True:
        candidate = random.getrandbits(bit_length)
        if is_prime(candidate):
            return candidate

def is_prime(n, k=5):
   
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
   
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    
    def miller_rabin_test(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False
    
    for _ in range(k):
        a = random.randrange(2, n - 1)
        if not miller_rabin_test(a):
            return False
    
    return True

def choose_public_exponent(eul):
 
    e = random.randrange(2, eul)
    while math.gcd(e, eul) != 1:
        e = random.randrange(2, eul)
    return e

def extended_euclidean_algorithm(a, b):
    
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def modular_inverse(e, eul):
 
    gcd, x, _ = extended_euclidean_algorithm(e, eul)
    if gcd == 1:
        return x % eul
    else:
        raise ValueError("No modular inverse exists")

def encrypt(m, public_key):
    n, e = public_key
    return pow(m, e, n)

def decrypt(c, private_key):
    n, d = private_key
    return pow(c, d, n)

public_key, private_key = generate_rsa_keys(bit_length=16)
print("Public Key (n, e):", public_key)
print("Private Key (n, d):", private_key)

m=int(input ("enter a plaintext message "))
c= encrypt(m, public_key)
print("Ciphertext:", c)
decrypted_message = decrypt(c, private_key)
print("Decrypted message:", decrypted_message)
