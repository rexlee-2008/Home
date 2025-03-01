n=int(input())
d={}
for i in range(n):
   t=input().split()
   d[i+1]=[t[0],t[1:]]
print(d)

m=int(input())
f=0
x=0
flag1=0
flag2=0
for i in range(m):
   l=input().split()
   k=l[0]
   if f==1 and x!=k:
      x=0
      f=0
   num=l[1]
   if k=="B":
      a,b=l[2],l[3]
   elif k=="M":
      a,b=l[2],l[3]
      if flag1==1:
         flag1=2
      flag1=1
   elif k=="E":
      a=l[2]
      if flag2==1:
         flag2=2
      flag2=1
   elif k=="R":
      a=l[2]
      x=k
      f=1
   