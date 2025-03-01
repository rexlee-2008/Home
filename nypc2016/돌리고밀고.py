from collections import deque
n=int(input())
m=int(input())
arr=[]
temp=[]
for i in range(n):
   t1=[]
   t2=[]
   for j in input():
      t1.append(j)
      t2.append(0)
   arr.append(t1)
   temp.append(t2)
   
   
for k in range(m):
   l=[]
   for i in range(len(arr)):
      if arr[i]!=["."]*n:
         flag=0
         for j in range(len(arr[i])-1,-1,-1):
            if arr[i][j]!=".":
               d=deque(arr[i])
               #print(d,arr[i],j)
               #if j==0:
                  #d.rotate(-1)
               #else:
               d.rotate(n-j-1)
               #print(j)
               l.append(list(d))
               flag=1
               break
         if flag==0:
            l.append(arr[i])
      else:
         l.append(arr[i])
   print()
   for q in l:
      print(q)
   print()
   arr=temp
   for i in range(len(l)):
      for j in range(len(l[i])):
         arr[i][j]=l[n-j-1][i]
   print()
   for i in arr:
      print(i)
   print()
   print()
   print()
   print()
'''
7
2
.......
.......
...A...
...B...
..ACA..
..BBB..
.AAAAA.
'''


