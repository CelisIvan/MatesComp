#import NumPy as np
def buildStateTransition(x,letter,num,d):
    print("How many elements can you reach from state q" + str(x+1) + " with "+str(letter))
    lst = [] 
    n = int(input())  
    if(n>num):
        while(n>num):
            print("That's not possible. The automaton has not that many states, try again.")
            print("How many elements can you reach from state q" + str(x+1) + " with "+str(letter))
            n = int(input())
    if(n<=num):
        for i in range(0, n):
            print("Write the number of the state "+ str(i+1)+" reacheable") 
            ele = int(input()) 
            lst.append(ele) # adding the element 
    elif(n==0):
        lst.insert(0,"None")
        lst.sort()
    if(letter=='a'):
        d[x].insert(0,lst)
    elif(letter=='b'):
        d[x].insert(1,lst)
    else:
        d[x].insert(2,lst)
    return None

def buildNFATF (d,closure,m):
    
    for i in range(num):
        for j in range(2):
            e1 = set()
            e2 = set()
            for item1 in closure[i]:
                e1.update(closure[item1-1])
            for item2 in e1:
                e2.update(d[item2-1][j])
                e3 = set()
            for item3 in e2:
                e3.update(closure[item3-1])
            if(j==0):
                m[i].insert(0,list((e3)))
            elif(j==1):
                m[i].insert(1,list((e3)))
    return None

num=int(input("Enter how many states: "))
d = [[] for j in range(num)]

for x in range(0, num):
    for letter in 'abE':
            buildStateTransition(x,letter,num,d)
print("E - TRANSITION FUNCTION")
print("          a  |  b  | epsilon")
print("_____________________________")
for k in range(num):
    print("state q"+str(k+1)+":"+str(d[k]))

print("------------------------------------")
print("E - Closure:")

closure = [[] for j in range(num)]
for j in range(num):
    for item in d[j][2]:
        closure[j].append(item)

for x in range(num):
    print("E - closure (q"+str(x+1)+"):"+str(closure[x]))
print("------------------------------------")

m=[[]for k in range(num)]

buildNFATF(d,closure,m)

print("TRANSITION FUNCTION")
print("          a  |  b")
print("----------------------")
for k in range(num):
    print("state q"+str(k+1)+":"+str(m[k]))