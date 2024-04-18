import random
import math
import time

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



def generate_rsa_keys(bit_length=16):
    # start_time = time.time()

    p = int(input("Enter a prime number (p): "))
    if p is is_prime:
        return True 
    else: 
        quit
    # print(is_prime(p))
    q = int(input("Enter another prime number (q): "))
    print(is_prime(q))
    n = p * q
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
    # end_time = time.time()
    # print("Time taken by generate_rsa_keys: ", end_time - start_time)
    return public_key, private_key


# def generate_prime_number(bit_length):
#     while True:
#         candidate = random.getrandbits(bit_length)
#         if is_prime(candidate):
#             return candidate

# def is_prime(n, k=5):
   
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0:
#         return False
    
   
#     r = 0
#     d = n - 1
#     while d % 2 == 0:
#         d //= 2
#         r += 1
    
    # def miller_rabin_test(a):
    #     x = pow(a, d, n)
    #     if x == 1 or x == n - 1:
    #         return True
    #     for _ in range(r - 1):
    #         x = pow(x, 2, n)
    #         if x == n - 1:
    #             return True
    #     return False
    
    # for _ in range(k):
    #     a = random.randrange(2, n - 1)
    #     if not miller_rabin_test(a):
    #         return False
    
    # return True


def choose_public_exponent(eul):
    # start_time = time.time()

    e = random.randrange(2, eul)
    while math.gcd(e, eul) != 1:
        e = random.randrange(2, eul)
    # end_time = time.time()
    # print("Time taken by generate_rsa_keys: ", end_time - start_time)
    return e


def extended_euclidean_algorithm(a, b):
    # start_time = time.time()

    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    # end_time = time.time()
    # print("Time taken by generate_rsa_keys: ", end_time - start_time)

    return gcd, x, y




def modular_inverse(e, eul):
    gcd, x, _ = extended_euclidean_algorithm(e, eul)
    if gcd == 1:
        return x % eul
    else:
        raise ValueError("No modular inverse exists")
    


# def encrypt(m, public_key):
#     n, e = public_key
#     return pow(m, e, n)

# def decrypt(c, private_key):
#     n, d = private_key
#     return pow(c, d, n)


def encrypt(m, public_key):
    # start_time = time.time()

    n, e = public_key
    if m >= n:
        print( ValueError(f"the number entered cannot be greater than {n}"))
        # end_time = time.time()
        # print("Time taken by generate_rsa_keys: ", end_time - start_time)
    return pow(m, e, n)



def decrypt(c, private_key):
    # start_time = time.time()
    n, d = private_key
    # end_time = time.time()
    # print("Time taken by generate_rsa_keys: ", end_time - start_time)
    return pow(c, d, n)


public_key, private_key = generate_rsa_keys(bit_length=16)
print("Public Key (n, e):", public_key)
print("Private Key (n, d):", private_key)

m=int(input ("enter a plaintext message "))
c= encrypt(m, public_key)
print("Ciphertext:", c)
decrypted_message = decrypt(c, private_key)
print("Decrypted message:", decrypted_message)
