n=int(input())
c=input()
print(c)
l=[]
left, right=0, n-1
f=1

while left<=right:
    if f:
         l.append(c[left])
         left+=1
    else:
        if c[left]<=c[right]:
            left+=1
        else:
            right-=1
    #print(f)
    f=not f
    #print(l)
print(''.join(l))