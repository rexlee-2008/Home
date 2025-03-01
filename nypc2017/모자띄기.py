n,m=map(int,input().split())
l=[]
t=[0]*n
c=0
for i in range(n):
   l.append(int(input()))
k=0
while(1):
   for i in range(n):
      if t[i]==l[i]:
         c+=1
         t[i]=0
      t[i]+=1
   if c>=m:
      print(k)
      break
   k+=1
'''
1 10
30

2 10
1
11

2 10
1
9
'''