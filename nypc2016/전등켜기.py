m,n=map(int,input().split())
l=[]
flag=0
for i in range(n):
   t=[]
   for j in input():
      t.append(j)
   l.append(t)
for i in range(m):
   # direction 0=u, 1=r, 2=d, 3=l
   x,y,direction=0,i,0
   while(1):
      if l[x][y]=="/":
         direction+=1
         if direction==4:
            direction=0
      elif l[x][y]=="\\":
         direction-=1
         if direction==-1:
            direction=3
      elif l[x][y]=="O":
         print("U",i)
         flag=1
         break
      if direction==0:
         if x==n-1:
            break
         x+=1
      if direction==1:
         if y==0:
            break
         y-=1
      if direction==2:
         if x==0:
            break
         x-=1
      if direction==3:
         if y==m-1:
            break
         y+=1
   if flag==1:
      break
'''
5 4
.....
/...
/.O..
....
'''