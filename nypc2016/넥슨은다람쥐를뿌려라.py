n=int(input())
l=[]
c=0
for i in range(n):
   t=[]
   for j in input():
      if j=="C":
         c+=2
      t.append(j)
   l.append(t)
#print(l)
if c!=0:
   t=l
   for i in range(len(t)):
      #print(i)
      for j in range(len(l[i])):
         if l[i][j]=="." and c!=0:
            l[i][j]="D"
            c-=1
         print(l[i][j],end=" ")
      print()
      
            
            
            
      
'''
5
.....
.....
.C...
.....
.....
'''