n = int(input())
t = list(map(int, input().split()))
order = list(map(int, input().split()))
d = {}
l = []
c = 0

for i in range(n):
   d[order[i]]=t[i]

for i in range(n):
   l.append(d[i+1])
   
#print(d,l)
while(1):
   t = sorted(l)
   if l == t:
      break
   for i in range(n-1):
      if l[i]>l[i+1]:
         for j in range(l[i]+1):
            l[i]-=1
            c+=1
            if l[i]<l[i+1]:
               break
      #print(l)
      #print(t,l)
   #print()
print()
print()

f=0
for i in l:
   if i<1:
      print(-1)
      f=1
      break
if f == 0:
   print(l,c)
   
'''
5
3 5 2 6 4
1 3 2 5 4
'''