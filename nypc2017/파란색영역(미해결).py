def dfs(l, x, y):
    if x < 0 or x >= len(l) or y < 0 or y >= len(l[0]) or l[x][y] == 0:
        return 0
    l[x][y] = 0
    c = 1

    c += dfs(l, x - 1, y)
    c += dfs(l, x + 1, y)
    c += dfs(l, x, y - 1)
    c += dfs(l, x, y + 1)

    return c

#def f(x1,y1,l1,x2,y2,l2):
    #x1,y1,l1=a
    #x2,y2,l2=b
    return not (x1+l1<x2 or x2+l2<x1 or y1+l1<y2 or y2+l2<y1)

n=int(input(()))
m=0
l=[]
t=[]

for i in range(n):
    l.append(list(map(int,input().split())))


'''
3
1 1 1
2 2 1
4 1 1

5
1 1 2
2 2 2
4 1 1
5 2 1
5 2 2
'''