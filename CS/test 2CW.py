import random
import math
import time

bits= int(input("choose between an 8 or 16 bit length: "))
if bits != 8:
    if bits != 16:
        raise ValueError("Input can only be 8 or 16")

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

def generate_rsa_keys():

    p = int(input("Enter a prime number (p): "))
    if not is_prime(p):
        print("p is not a prime number.")
        raise ValueError("The number is not prime")
    q = int(input("Enter another prime number (q): "))
    if not is_prime(q):
        print("q is not a prime number.")
        raise ValueError("The number is not prime")
    n = p * q
    if n>255 and bits == 8:
        print("n should not exceed 255")
        raise ValueError(f"{n} is not an 8 bit number")
    elif n>65535 and bits == 16:
        print("n should not exceed 65535")
        raise ValueError(f"{n} is not an 16 bit number")
    eul = (p - 1) * (q - 1)
    e = choose_public_exponent(eul)
    
    start = time.perf_counter()

    d = modular_inverse(e, eul)

    end = time.perf_counter()
    runtime = end - start
    print(f"The runtime for getting d is {runtime} seconds")

    if e == d:
        e = random.randrange(2, eul)
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

def choose_public_exponent(eul):
    e = random.randrange(2, eul)
    while math.gcd(e, eul) != 1:
        e = random.randrange(2, eul)
    print(f"Make sure that the plaintext is greater than {e}")
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
    if m >= n:
        print( ValueError(f"The number entered cannot be greater than {n-1}"))
    return pow(m, e, n)

def decrypt(c, private_key):
    n, d = private_key
    return pow(c, d, n)
public_key, private_key = generate_rsa_keys()

print("Public Key (n, e):", public_key)
print("Private Key (n, d):", private_key)

m=int(input ("Enter a plaintext message: "))
c= encrypt(m, public_key)
print("Ciphertext:", c)
decrypted_message = decrypt(c, private_key)
print("Decrypted message:", decrypted_message)

