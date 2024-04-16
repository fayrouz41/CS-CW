import math 
p= int (input("enter a prime number"))
q= int (input("enter a prime number"))
n = p*q
eul= (p-1)*(q-1)
# e=3 

# def gcd (a,b):
#     while b != 0:
#         a ,b = b, a%b
#     return a 
while e < eul:
    if gcd(e,eul)==1:
        break
    else: 
        e+=1
d=pow(e,-1,eul)
print(f"public:{n,e}")
print(f"private:{n,d}")
m=11
c=pow(m,e,n)
M=pow(c,d,n)
print(m,c,M)


def extended_gcd(a,b): 
    x0,x1,y0,y1 = 1, 0, 0, 1
    while b: 
        q, a, b = a // b, b, a%b
        x0, x1 = x1, x0 - q* x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

e=17
eul=40
gcd, x, y =extended_gcd(e,eul)

def calculate_private_exponent(e, phi_N):
    gcd, x, _ = extended_gcd(e, phi_N)
    if gcd != 1:
        raise ValueError("Public exponent and totient are not coprime.")
    return x % phi_N = x

print(f"The private exponent (d) is:{private_exponent}")
