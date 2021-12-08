
class Node:
    def __init__(self, first_name, second_name, phone_nr) -> None:
        self.left = None
        self.right = None
        self.first_name = first_name
        self.second_name = second_name
        self.phone_nr = phone_nr

    def __repr__(self) -> str:
        return f"Name: {self.first_name} {self.second_name}\nPhone number: {self.phone_nr}"


def search(node, first_name) -> Node:
    """Search throught the BST with the help of a given key"""

    #if root is null/empty
    if node is None or node.first_name == first_name:
        return node

    #Key is greater than root key
    if node.first_name < first_name:
        return search(node.right, first_name)

    #key is smaller than root's key
    return search(node.left, first_name)


def insert(node, first_name, second_name, phone_nr):
    """Insert a key into the BST"""
    if node is None:
        return Node(first_name, second_name, phone_nr)

    else:
        if node.first_name == first_name:
            return node

        #if key is greater than current node key.
        elif node.first_name < first_name:
            node.right = insert(node.right, first_name, second_name, phone_nr)

        else:
            node.left = insert(node.left, first_name, second_name, phone_nr)
        
    return node


#Hur funkar denna?
def inorder(root):
    """Prints the BST in ascending order."""
    if root:
        inorder(root.left)
        print(f"Name: {root.first_name} {root.second_name}.\nPhone number: {root.phone_nr}")
        inorder(root.right)

def min_value_node(node):
    """Finds the node with the smallest value from current node"""
    current = node
    while current.left is not None:
        current = current.left

    return current

def delete_node(root, first_name):
    """Deletes a node from the BST"""
    #print(f"\nDelete result: {first_name}.")
    #Base case
    if root is None:
        return root

    #If first name is less than root first name
    #Then the first name is in the side side of the BST
    if first_name < root.first_name:
        root.left = delete_node(root.left, first_name)

    elif first_name > root.first_name:
        root.right = delete_node(root.right, first_name)

    else:
        #Nodes with only one child or no children/leaf.
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        
        root.first_name = temp.first_name
        root.second_name = temp.second_name
        root.phone_nr = temp.phone_nr

        #Delete the inorder successor.
        root.right = delete_node(root.right, temp.first_name)

#For resting purposes
def main():
    #     50
    #    /  \
    #  30    70
    #  / \   / \
    # 20 40 60 80
    
#    r = Node(50)
#    r = insert(r, 30)
#    r = insert(r, 20)
#    r = insert(r, 40)
#    r = insert(r, 70)
#    r = insert(r, 60)
#    r = insert(r, 80)

    r = Node("Pappa", "Efternamn", 12345)
    r = insert(r, "Arman", "Iqbal", 7654321)
    r = insert(r, "Xena", "Princess", 1726758)
    r = insert(r, "Zebra", "Svenson", 771628)

  
    # Print in order traversal of the BST
    inorder(r)

    node = search(r, "Arman")
    print("\nSearch result:")
    print(node)

    
    r = delete_node(r, "Arman")

    inorder(r)

if __name__ == "__main__":
    main()