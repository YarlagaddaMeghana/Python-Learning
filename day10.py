n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print()


for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print('1',end=' ')
    print()

print()

c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=' ')
        c+=1
    print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(i-1,0,-1):
        print(j,end=' ')
    print()
