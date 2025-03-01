n,e=map(int,input().split())

l=[]
t=[]

for i in range(n):
    x,y=map(int,input().split())
    t.append((x,y))
    l.append(float('inf'))

print(l)
l[0]=1

for i in range(1, n):
    for j in range(i):
        if abs(t[i][1]-t[j][1])<=e:
            l[i]=min(l[i],l[j]+1)

if l[n-1]==float('inf'):
    print(-1)
else:
    print(l[n-1])


'''
4 1
1 2
2 3
3 2
4 -1
'''