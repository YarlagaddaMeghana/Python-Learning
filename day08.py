#1. print numbers from 1 to 10 on same line
n=10
for i in range(1,n+1):
    print(i,end=' ')
print()


#2. print even numbers from 5 to 30 in one line
for i in range(5,31,1):
    if i%2==0:
        print(i,end=' ')
print()


#3. print odd numbers from 5 to 30 in one line
for n in range(5,31,1):
    if n%2==1:
        print(n,end=' ')
print()


#4. print numbers divisible by 5 from 1 to 30 in one line
for i in range(1,31):
    if i%5==0:
        print(i,end=' ')
print()


#5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
for i in range(1,101):
    if i%5==0 and i%7==0:
        print(i,end=' ')
print()


#6. sum of numbers from 10 to 25 
sum=0
for i in range(10,26):
    sum=sum+i
print(f'sum of numbers from 10 to 25 is {sum}')
print()


#7. sum of numbers in list [4,3,2,5,6,7] 
l=[4,3,2,5,6,7]
sum=0
for i in range(len(l)):
    sum=sum+l[i]
print(f'sum of numbers in given list is {sum}')
print()


#8. multiplication table of a number 
n=int(input())
for i in range(1,11):
    print(f'{n} x {i} = {n*i}')
print()


#9. factorial
n=int(input())
fact=1
if n>0:
    for i in range(1,n+1):
        fact=fact*i
    print(f'factorial of {n} is {fact}')
else:
    print("Enter valid number")
print()


#10. fibonacci 
n=int(input())
a=0
b=1
if n>0:
    for i in range(n):
        print(a,end=' ')
        a,b=b,a+b
    print()



#11. reverse a string
s='meghu'
rev=''
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
print(f'reversed string is {rev}')


#12. count vowels in a string
s=str(input())
count=0
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        count=count+1
print(f'count of vowels is {count}')


#13. count z's and y's in a string
s=str(input())
count=0
for i in range(len(s)):
    if s[i] in "zZyY":
        count=count+1
print(f'count of z s and y s is {count}')


#14. check whether a number is prime number or not 
n=int(input())
if n>0:
    for i in range(2,n):
        if n%i==0:
            print("Not a prime")
            break
    else:
        print("prime ")
else:
    print("enter valid number")


#15. print 1 to 10 with while loop
n=1
while n<=10:
    print(n,end=' ')
    n+=1


#16. print even numbers from 1 to 10
n=1
while n<=10:
    if n%2==0:
        print(n,end=' ')
    n+=1


#17. print numbers divisible by both 5 and 7 from 1 to 500 
n=1
while n<=500:
    if n%5==0 and n%7==0:
        print(n,end=' ')
    n+=1


#18. count digits
n=int(input())
count=0
while n>0:
    rem=n%10
    count+=1
    n=n//10
print(count)


#19. reverse a number
n=int(input())
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)


#20. palindrome number
n=int(input())
Num=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if Num==rev:
    print("palindrome")
else:
    print("Not palindrome")


#21. palindrome string without slicing, without built in function
s=str(input())
n=len(s)-1
rev=''
while n>=0:
    rev=rev+s[n]
    n=n-1
print(rev)


#22. armstrong number
n=int(input())
num=n
count=0
while n>0:
    rem=n%10
    count=count+rem**3
    n=n//10
if(num==count):
    print("Armstrong number")
else:
    print("Not Armstrong number")
        


