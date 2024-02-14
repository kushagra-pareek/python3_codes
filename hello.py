# so variable is somethingg that can be changed
#initially the variable x has value 4*3 and prints that value
x=4*3
print (x)
# however variable changes value to a string  "kuch bhi lelo" and prints that afterwards
x="kuch bhi lelo"
print (x)

# key points:
# python is strong and dynamic language as it does not need to specify the data type of the variable
"""Python is both a strongly typed and a dynamically typed language. Strong typing means that variables 
do have a type and that the type matters when performing operations on a variable. Dynamic typing means 
that the type of the variable is determined only during runtime."""


#booleans are used to indicate true or false condition
x=True
y=False
# here both true and false are case sensitive

#Comparisons
print(f'x={x}')
print(f'y={y}')

print(f'Equal = {x==y}')
print(f'Not Equal = {x!=y}')

print(f'greater than = {x>y}')
print(f'greater than equal to = {x>=y}')

print(f'less than = {x<y}')
print(f'less than equal to = {x<=y}')

#Types of numbers
# int
ival = 50
print(f'ival ={ival}')
#float
fval =3.14
print(f'fval ={fval}')
#complex
cval= 5+6j
print(f'cval = {cval}')
cval=complex(5,3)
print(f'real ={cval.real} , imag ={cval.imag}')
#import a module
import os 
d=os.getcwd()
print(f'current working directory: {d}')

#change folders
os.chdir('..')
print(f'current working directory:{os.getcwd()}')

#listdirectory
for f in os.listdir():
    print(f)
    print(f'path:{os.path.abspath(f)}')
    if os.path.isdir(f) : print(f'dir:{f}')
    if os.path.isfile(f) : print(f'file:{f}')
    if os.path.islink(f) : print(f'link:{f}')