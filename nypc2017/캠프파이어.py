n = int(input())
l = []
print("S_OK")
for i in range(n):
   t, x, y = map(int, input().split())
   if i == 0:
      l.append([t, x, y])
   else:
      flag = 0
      d=[]
      for j in range(len(l)):
         if l[j][0] + 300 <= t:
            d.append(j)
            continue
         elif ((x - l[j][1]) ** 2 + (y - l[j][2]) ** 2) ** .5 < 5:
            flag = 1
            break
      for k in d:
         l.remove(l[k])
      if flag == 1:
         print("E_FAILED")
      else:
         print("S_OK")
         l.append([t,x,y])
'''
9
0 0 0
0 0 0
2 4 0
4 2 3
7 5 0
12 -3 -4
299 2 3
300 0 0
301 5 2
'''