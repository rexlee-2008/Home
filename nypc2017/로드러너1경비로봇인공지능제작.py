from collections import deque

n, m = map(int, input().split())
h, v, f = map(int, input().split())

map = []
for i in range(m):
   temp = []
   for j in input():
      temp.append(j)
   map.append(temp)
#print(map)
for i in range(m):
    for j in range(n):
        if map[i][j] == 'R':
            runner = (i, j)
        elif map[i][j] == 'G':
            guard = (i, j)
#print(map)
d = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]



def f(pos):
    l = deque([(pos[0], pos[1], "")])  # (x, y, path)
    print(l)
    visited = []
    for i in range(m):
       visited.append([False]*n)
    #print(visited)
    
    visited[pos[0]][pos[1]] = True
    
    while l:
        x, y, z = l.popleft()
        
        if (x, y) == runner:
            return z
        
        for x1, y1, i in d:
            x2, y2 = x + x1, y + y1
            
            print(x2,y2,i,z)

            if 0 <= x2 < m and 0 <= y2 < n and not visited[x2][y2]:
               if map[x2][y2] != 'B':
                  if z == 'U' and map[x][y] != 'H':
                     continue
                  visited[x2][y2] = True
                  l.append((x2, y2, z + i))
    
    return "X"


print(f(guard))


'''
5 5
1 1 1
BBBBB
B.R.B
B.BHB
BG.HB
BBBBB
'''