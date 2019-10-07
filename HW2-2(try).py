#import NumPy as np

num=int(input("Enter how many states: "))

d = [[] for j in range(num)]

for x in range(0, num):
    for i in range(3):
        if i == 0:
            print("How many elements can you reach from state " + str(x+1) + " with 'a'")
            lst = [] 
            # number of elemetns as input 
            n = int(input())  
            # iterating till the range 
            if(n!=0):
                for i in range(0, n):
                    print("Write the number of the state"+ str(i+1)) 
                    ele = int(input()) 
                    lst.append(ele) # adding the element 
            elif(n==0):
                lst.insert(0,"None")
            d[x].insert(0,lst)
        elif i == 1:
            print("How many elements can you reach from state " + str(x+1) + " with 'b'")
            lst = [] 
            # number of elemetns as input 
            n = int(input())  
            if(n!=0):
                # iterating till the range 
                for i in range(0, n):
                    print("Write the number of the state"+ str(i+1)) 
                    ele = int(input()) 
                    lst.append(ele) # adding the element 
            elif(n==0):
                lst.insert(0,"None")
            d[x].insert(1,lst)
        else:
            print("How many elements can you reach from state " + str(x+1) + " with 'epsilon'")
            lst = [] 
            # number of elemetns as input 
            n = int(input())  
            if(n!=0):
                # iterating till the range 
                for i in range(0, n):
                    print("Write the number of the state"+ str(i+1)) 
                    ele = int(input()) 
                    lst.append(ele) # adding the element 
            elif(n==0):
                lst.insert(0,"None")
            d[x].insert(2,lst)
print("a     b     epsilon")
for k in range(num):
    print(d[k])
