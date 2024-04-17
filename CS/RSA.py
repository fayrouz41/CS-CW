import math
import random

def prime(z):
    if z <= 1:
        return False
    for i in range(2, int(z**0.5) + 1):
        if z % i == 0:
            return False
    return True

def extended_gcd(a,b): 
    x0,x1,y0,y1 = 1, 0, 0, 1
    while b: 
        q, a, b = a // b, b, a%b 
        x0, x1 = x1, x0 - q* x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def mod_inverse(a,m):
    gcd, x, _= extended_gcd(a,m)
    if gcd!=1:
        raise ValueError("Invers does not exist.")
    else: 
        return x%m

m=int(input ("enter a plaintext integer that will be encrypted"))
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))

if not (prime(p) and prime(q)):
    print("Both p and q must be prime numbers.")

n = p*q
eul= (p-1)*(q-1)

e = 17

   
while e < eul:
    if extended_gcd(e,eul)==1:
        break
    else: 
        e+=1



d=mod_inverse(e, eul)
print(f"public:{n,e}")
print(f"private:{n,d}")

c=pow(m,e,n)
M=pow(c,d,n)
print(m,c,M)

   
