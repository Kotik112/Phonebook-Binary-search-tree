
class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key


def search(root, key):
    """Search throught the BST with the help of a given key"""

    #if root is null/empty
    if root is None or root.val == key:
        return root

    #Key is greater than root key
    if root.val < key:
        return search(root.right, key)

    #key is smaller than root's key
    return search(root.left, key)


def insert(root, key):
    """Insert a key into the BST"""
    if root is None:
        return Node(key)

    else:
        if root.val == key:
            return root

        #if key is greater than current node key.
        elif root.val < key:
            root.right = insert(root.right, key)

        else:
            root.left = insert(root.left, key)
        
    return root


#Hur funkar denna?
def inorder(root):
    """Prints the BST in ascending order."""
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


#For resting purposes
def main():
    #    50
    #  /     \
    # 30     70
    #  / \ / \
    # 20 40 60 80
    
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    
    # Print inoder traversal of the BST
    inorder(r)

if __name__ == "__main__":
    main()