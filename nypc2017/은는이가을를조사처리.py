input = input()

l = {}

for i in input:
    if i.startswith("set"):
        a,b,c = i.split(maxsplit=2)
        print(a,b,c)
        print()
        l[b] = c
    elif i.startswith("print"):
        print(i.split(maxsplit=1)[1].format(**l))
    elif i == "end":
        break