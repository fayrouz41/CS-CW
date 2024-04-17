import math 
p= int (input("enter a prime number"))
q= int (input("enter a prime number"))
def prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
if prime(p): 
    print (True)
else:
    print (f"{p} is not prime")
if prime(q): 
    print (True)
else:
    print (f"{q} is not prime")


n = p*q
eul= (p-1)*(q-1)
# e=3 

# def gcd (a,b):
#     while b != 0:
#         a ,b = b, a%b
#     return a 
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

def calculate_private_exponent(e, ):



# ..
while e < eul:
    if extended_gcd(e,eul)==1:
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

   
