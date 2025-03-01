n=int(input())
l=[]
for i in range(n):
   s=input()
   if s in l:
      continue
   else:
      l.append(s)
#print(l)
if len(l)>3:
   print("invalid")
else:
   print("valid")