def abs(x):
    if x<0:
        return -x
    else:
        return x

n,k=map(int,input().split())
l=[]
a=[]
b=[]
for i in range(n):
   l.append([0]*n)
for i in range(k):
   x,y=map(int,input().split())
   a.append([x,y])
for i in range(k):
   x,y=map(int,input().split())
   b.append([x,y])
print(a,b)

m=0

for i in range(k):
   x1,y1=a[i][0],a[i][1]
   for j in range(k):
      x2,y2=b[j][0],b[j][1]
      print(x1,y1,x2,y2)
      f=abs(x1-x2)+abs(y1-y2)
      if f>m:
         m=f
      
      print(f)

print()
print(m)


'''
5 3
1 2
2 3
3 1
3 5
4 5
5 4
'''