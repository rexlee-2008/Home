def create_binary_tree(n):
    tree = [i for i in range(1, n + 1)]
    l = []

    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        l.append([tree[i], tree[left] if left < n else None, tree[right] if right < n else None])
    
    return l

n = 10
tree = create_binary_tree(n)

for node in tree:
    print(node)









def dfs():
    




'''
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
  / \ / \
 8  9 10
'''