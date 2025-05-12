def palind(r):
    e=len(r)-1
    a=0
    while(a<e):
        if (r[a]!=r[e]):
            return False
        a+=1
        e-=1
    return True

r=(1,2,3,3,2,1)

if (palind(r)):
    print("The Tuple is flip flop")

else:
    print("The Tuple is not flip flop")