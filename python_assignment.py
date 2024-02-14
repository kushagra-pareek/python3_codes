#level 1
# Q1 : For a list L = [10, 20, 30, 40,-1,50,-2,-5] do below task:
#       A] : Multiply every elements in list by 2 and save these elements in other list
#            L1 using list Comprehension, and print L1
#        B]: Multiply every elements in list by 2 and save only elements which are positive in other list L2
#           using list Comprehension , and print L2


L=[10, 20, 30, 40,-1,50,-2,-5]
L1=[]
L2=[]
#A]
print(L)
for i in L:
    L1.append(i*2)
print(L1)
#B]
for i in L1 :
    if i > 0:
        L2.append(i)
print(L2)

 # Q2 : Write a Lambda function to find multiplication of two number.
multiply2nos=lambda x,y: x*y

result=multiply2nos(2,3)
print(result)

# Q3 : A] Write a function FINDMAX(a,b) to  find maximum of given number a and b
#      B] Using map function and FINDMAX(a,b) function using find  maximum value in list L = [10, 20, 30, 40,-1,50,-2,-5]

#A] 
def findmax(a,b):
    return a if a > b else b

res=findmax(3,5)
print(res)
#B]
out=max(map(findmax,L[:-1],L[1:]))
print(out)


# Q4 : A] Write a function IsPositive(a) which will  take one parameter and return True if number is greater than zero
#       Else return False
#      B] Using filer function and  IsPositive function find only positive number is list L = [10, 20, 30, 40,-1,50,-2,-5]

#A]
def ispositive(a):
  return a>0
output=ispositive(-2)
print(output)
#B]
L=[10, 20, 30, 40,-1,50,-2,-5]
positive_numbers = list(filter(ispositive, L))
print(positive_numbers)
from functools import reduce


#Q5  : A] Write a function MUL(a,b) to multiply two given numbers
#      B] Using reduce function and MUL(a,b) function find multiplication of all elements of the list
#A]
def MUL(a,b):
    r=a*b
    return r
output1=MUL(3,4)
print (output1)
#B]
product=reduce(MUL,L)
print(product)


#level 2

#1.Calculate the factorial of a number by creating a function ‘calFactorial’.

def calfactorial(x):
    factorial=1
    if x<0:
        print("factorial is not possible")
    elif x==0:
        return 1
    else:
        for i in range(1,x+1):
            factorial*=i
        return factorial
        
res1=calfactorial(3)
print(res1)

#2.Write a function Greet , which should take one argument as language , In function body check if language is ‘Hindi’ print ‘Namaskar’  ,else if  language is ‘English’ print ‘Hello’,else print Error message as wrong language.
def greet (language):
    if language=='hindi':
        print("Namaskar")
    elif language == 'english':
        print("Hello")
    else:
        print("Wrong language")

greet('hindi')
greet('english')
greet('french')


def print_big_enough(L, x):
    """Print elements in the list that are at least as large as x."""
    for num in L:
        if num >= x:
            print(num)

# Example usage
L = [4, 20, 31, 10, 100, 200]
x = 3
print_big_enough(L, x)

