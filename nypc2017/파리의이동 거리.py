n=int(input())
for i in range(n):
   a,b=map(int,input().split())
   x,y,z=map(int,input().split())
   print((x+y)/(b-a))
   print(((b-a)/(x+y))*z)
'''
2
-5 8
3 4 5
-4 8
4 5 1
'''