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
    if(letter=='a'):
        d[x].insert(0,lst)
    elif(letter=='b'):
        d[x].insert(1,lst)
    else:
        d[x].insert(2,lst)
    return None

def buildNFATF (d,closure,m):
    e1 = set()
    e2 = set()
    for i in range(num):
        print("i"+str(i))
        for j in range(2):
            for item in closure[i]:
                e1.update(d[a-1][j])
                for item in e1:
                    b=item
                    e2.update(closure[b-1])
            m[i][j].extend(e2)
    return None

num=int(input("Enter how many states: "))
d = [[] for j in range(num)]

for x in range(0, num):
    for letter in 'abE':
            buildStateTransition(x,letter,num,d)
print("E - TRANSITION FUNCTION")
print("          a    b   epsilon")
for k in range(num):
    print("state q"+str(k+1)+":"+str(d[k]))

print("------------------------------------")
print("E - Closure:")

closure = [[] for j in range(num)]
for j in range(num):
    for item in d[j][2]:
        closure[j].append(item)

print (closure)

for x in range(num):
    print("E - closure (q"+str(x+1)+"):"+str(closure[x]))
print("------------------------------------")

m=[[]for k in range(num)]

#buildNFATF(d,closure,m)

print("E - TRANSITION FUNCTION")
print("          a    b")
for k in range(num):
    print("state q"+str(k+1)+":"+str(m[k]))