
class Node:
    def __init__(self, first_name, second_name, phone_nr) -> None:
        self.left = None
        self.right = None
        self.first_name = first_name
        self.second_name = second_name
        self.phone_nr = phone_nr


def search(root, first_name):
    """Search throught the BST with the help of a given key"""

    #if root is null/empty
    if root is None or root.first_name == first_name:
        return root

    #Key is greater than root key
    if root.first_name < first_name:
        return search(root.right, first_name)

    #key is smaller than root's key
    return search(root.left, first_name)


def insert(root, first_name, second_name, phone_nr):
    """Insert a key into the BST"""
    if root is None:
        return Node(first_name, second_name, phone_nr)

    else:
        if root.first_name == first_name:
            return root

        #if key is greater than current node key.
        elif root.first_name < first_name:
            root.right = insert(root.right, first_name, second_name, phone_nr)

        else:
            root.left = insert(root.left, first_name, second_name, phone_nr)
        
    return root


#Hur funkar denna?
def inorder(root):
    """Prints the BST in ascending order."""
    if root:
        inorder(root.left)
        print(f"Name: {root.first_name} {root.second_name}.\nPhone number: {root.phone_nr}")
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