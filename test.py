def proc(x):
    x = 2*x*x
    return x

def main():
    num = 10
    num = proc(num)  # Assign the result back to num
    print(num)       # Print the updated value of num

main()

#5.Create a function AddList , which should take two argument as two Lists L1 and L2; add the corresponding elements of the list and save result in L3 and return the list L3. 
#Assume, L1 = [1,2,3,4] ,  L2 = [10,20,30,40]
#Hint: Use append function to extend new list.

def addlist(l1, l2):
    l3=[]
    if len(l1)!=len(l2):
        print("length of the list must be same")
    else:
        for i in range(len(l1)):
            l3.append(l1[i]+l2[i])
        return l3
L1 = [1,2,3,4] 
L2 = [10,20,30,40]  
num=addlist(L1, L2)
print(num)


