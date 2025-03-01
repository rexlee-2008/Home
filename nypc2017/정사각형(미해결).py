a,b,c,d,k=map(int,input().split())

c=0

for size in range(1,k+1):
    if size<=a and size<=b:
        c+=(a-size+1) * (b-size+1)
    if size<=b and size<=d:
        c+=(b-size+1) * (d-size+1)
    if size<=a and size<=d:
        c+=(a-size+1) * (d-size+1)
    if size<=c and size<=d:
        c+=(c-size+1) * (d-size+1)

print(c)