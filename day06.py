for x in 'rakesh':
    print(x, end=' ')  #r a k e s h
print()
for x in range(2, 7):
    print(x, end=' ')  #2 3 4 5 6
print()
for x in [1,2,3]:
    print(x, end=' ') #1 2 3
print()
for x in (4,5,6):
    print(x, end=' ') #4 5 6 
print()
for x in {7, 8, 9}:
    print(x, end=' ') # 7 8 9
print()
d = {1:'a', 2:'b', 3:'c'}
for x in d:
    print(x, end=' ')  #1 2 3
print()
for x in d.keys():
    print(x, end=' ')  #1 2 3 
print()
for x in d:
    print(d[x], end=' ') #a b c 
print()
for x in d.values():   
    print(x, end=' ')#a b c
print()
for x in d.items():     
    print(x, end=' ')#(1,'a') (2,'b') (3,'c')
print()
#index based for loop. 
l = [5,4,3,2,1]
#iterate from left to right 
for i in range(len(l)):
    print(l[i], end=' ')#5 4 3 2 1 
print()
#iterate from right to left 
for i in range(len(l)-1, -1, -1):
    print(l[i], end=' ') #1 2 3 4 5
print()
#iterate from 3rd element 
for i in range(2, len(l)):
    print(l[i], end=' ') #3 2 1
print()
#iterate in steps of 2
for i in range(0, len(l), 2):
    print(l[i], end=' ') #5 3 1
print()

#tricky
l = [1, 2, 3, 4, 5, 6]
for x in l:
    print(x) #1 3 5
    l.remove(x)

#Homework
t = (5,4,3,2,1) 
for x in t:
    print(x,end=' ')
print()
for x in range(len(t)-1,-1,-1):
    print(t[x],end=' ')
s = {5,4,3,2,1}
a=list(s)
print(a)
for x in a:
    print(x,end=' ')
print()
for x in range(len(a)-1,-1,-1):
    print(a[x],end=' ')
print()
d = {5:'e', 4:'d', 3:'c', 2:'b', 1:'a'}
for x in d:
    print(x,end=' ')
print()
for x in range(len(d)-1,-1,-1):
    print(list(d.keys())[x],end=' ')
print()
w = 'rakesh'
for x in w:
    print(x,end=' ')
print()
for x in range(len(w)-1,-1,-1):
    print(w[x],end=' ')
r = range(5,0,-1)
for x in r:
    print(x,end=' ')
print()
for x in range(1,6,1):
    print(x,end=' ')

print()

#continue 
for x in range(1,11):
    if x % 3 == 0:
        continue  # 1 2 4 5 7 8 10
    print(x,end=' ')    
print()
#break
for x in range(1,11):
    if x % 3 == 0:      
        break 
    print(x,end=' ')  # 1 2
print()
#pass 
for x in range(1,11):
    pass
a = 21
#else 
for x in range(1,11):
    if x % 3 == 0:
        continue 
    print(x, end=' ') #1 2 4 5 7 8 10 Loop completed successfully
else:
    print('Loop completed successfully') 
print() 
for x in range(1, 11):
    if x % 3 == 0:
        break 
    print(x, end=' ') #1 2
else:
    print('Loop completed successfully') 
print('\n') #new line
#assert
n = 10 
assert n > 5, 'N is not greater than 5' 
print('A')
assert n < 5, 'N is not lesser than 5' 
print('B') #N is not lesser than 5
