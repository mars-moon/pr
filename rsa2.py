def gcd(a,b):
    while 1==1:
        r = a%b # temp is r
        if r==0:
            return b
        else:
            a=b
            b=r
# step 1
P=101 # large prime numbers
Q=103 # large prime numbers

#step 2
n=P*Q
T=(P-1)*(Q-1) # phi_of_n

# step 3
e=2 # starting from 2
while e<T:
    if gcd(e,T)==1:
        break
    else:
        e+=1

print("e = ", e)

# step 4
k=1
while k<n:
    d=(1+(k*T))/e
    if d==int(d):
        break
    else:
        k+=1
print("d = ",d)

# d = pow(e, -1, T)

# step 5
msg=32
print(f'MSG={msg}')

cText=pow(msg,e,n)
print(f'cText={cText}') 

# step 6
dtext=pow(cText,int(d),n)
print(f'dText={dtext}')



