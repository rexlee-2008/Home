d={
    '0': {'segments': 6, 'on': {0, 1, 2, 3, 4, 5}},
    '1': {'segments': 2, 'on': {1, 2}},
    '2': {'segments': 5, 'on': {0, 1, 3, 4, 6}},
    '3': {'segments': 5, 'on': {0, 1, 2, 3, 6}},
    '4': {'segments': 4, 'on': {1, 2, 5, 6}},
    '5': {'segments': 5, 'on': {0, 2, 3, 5, 6}},
    '6': {'segments': 6, 'on': {0, 2, 3, 4, 5, 6}},
    '7': {'segments': 3, 'on': {0, 1, 2}},
    '8': {'segments': 7, 'on': {0, 1, 2, 3, 4, 5, 6}},
    '9': {'segments': 6, 'on': {0, 1, 2, 3, 5, 6}},
    '+': {'segments': 2, 'on': {3, 6}},
    '-': {'segments': 1, 'on': {6}}
}

# 성냥개비 변환 비용 계산
def f1(x, y):
   a = d[x]['on']
   b = d[y]['on']
   print(a,b)
   print(a-b,b-a)
   if a-b!={} and b-a!={}:
      return len(a - b) + len(b - a)-1
   else:
      return len(a - b) + len(b - a)



print(f1("2","3")) 



def f2(expression):
   l = []
   t=[]
   for i, s in enumerate(expression):
      if s in d:
         for j in d:
            if s != j:
               print(s,j)
               c = f1(s, j)
               if c <= 1:  # 성냥개비 1개 이동 제한
                  new_expression = expression[:i] + j + expression[i+1:]
                  l.append(new_expression)
                  t.append(eval(new_expression))
   return l,t

#print(f2("5000-7000+3000"))
#print(f1("2","3"))