def f(l,t):
   print(l,t)
   if len(t)==0:
      print("------------------------")
      return 1
   if t[0]==l[0]:
      del t[0],l[0]
      return f(l,t)
   if t[0]==l[-1]:
      del t[0],l[-1]
      return f(l,t)
   if t[0]!=l[0] and t[0]!=l[-1]:
      return 0


k=int(input())
for i in range(k):
   n=int(input())
   l=list(input())
   t=list(input())
   print(f(l,t))
   #while(1):
      
'''
2
6
abcbad
adb
6
abcbad
cba
'''