A = [0] + list(map(int,input().split()))

ans = 0

for i in range(1, 8):
    while A[i] != i:
       print(i,A[i])
       
'''
2 3 7 6 1 4 5
'''