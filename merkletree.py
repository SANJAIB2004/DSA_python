import hashlib

def sha256(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def build_merkel(leaves):
    hashed_leaves = [sha256(leaf) for leaf in leaves]
    # print(hashed_leaves)
    tree = hashed_leaves

    while len(hashed_leaves)>1:
        new_leaves = []

        if len(hashed_leaves)%2!=0:
            hashed_leaves.append(hashed_leaves[-1])

        for i in range(0,len(hashed_leaves),2):
            combined = hashed_leaves[i]+hashed_leaves[i+1]
            new_hash = sha256(combined)
            new_leaves.append(new_hash)

        hashed_leaves = new_leaves
        tree.append(hashed_leaves)

    return tree,hashed_leaves[0]

leaves = ['block a','block b','block c']
tree,root = build_merkel(leaves)

for i in tree:
    print(i)
print()

print(root)