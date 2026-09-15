n=int(input())
# right triangle
for i in range(1,n+1):
    print(i*'*')

print()

# inverted right triangle
for i in range(n,0,-1):
    print(i*'*')

print()

# triangle
for i in range(1,n+1):
    print((n-i)*' ' + i*'* ')

print()
# inverted triangle
for i in range(n,0,-1):
    print((n-i)*' '+i*'* ')

print()
# diamond
for i in range(1,n+1):
    print((n-i)*' ' + i*'* ')
for i in range(n-1,0,-1):
    print((n-i)*' '+i*'* ')
print()
# hollow square
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
print()

for i in range(1,n+1):
    print((n-i)*'*'+i*' '+(i-1)*' '+(n-i)*'*')

for i in range(n):
    if i==0:
        print((2*n-1)*'*',end=' ')
    else:
        print((n-i)*'*'+(2*i-1)*' '+(n-i)*'*',end=' ')
    print()
print()

for i in range(n):
    if i==n-1:
        print((2*n-1)*'*',end=' ')
    else:
        print((i+1)*'*'+(n+1-2*i+1)*' '+(i+1)*'*',end=' ')
    print()
print()
# star
for i in range(n):
    for j in range(n):
        if i==j or j==n-i-1 or i==n//2 or j==n//2:
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print() 

