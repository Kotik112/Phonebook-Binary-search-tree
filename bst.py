from typing import List

def set_with_fill(list, elem, idx):
    """Inserts or replaces an element into a list at a given index. Fills out 
    all the empty spots up to the element's index with None"""

    for _ in range((idx+1) - len(list)):
        list.append(None)

    list[idx] = elem

def list_get(list, idx, default):
    """Returns an element from a list or a default value, works like dict.get"""
    if len(list) > idx:
        return list[idx]
    else:
        return default
            
class Node:
    def __init__(self, first_name, second_name, phone_nr) -> None:
        self.left = None
        self.right = None
        self.first_name = first_name
        self.second_name = second_name
        self.phone_nr = phone_nr

    def __repr__(self) -> str:
        return f"\nName: {self.first_name} {self.second_name}\nPhone number: {self.phone_nr}"


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

    if first_name < node.first_name:
        node.left = insert(node.left, first_name, second_name, phone_nr)
    else:
        node.right = insert(node.right, first_name, second_name, phone_nr)
    
    #return (unchanged) node pointer
    return node

#Hur funkar denna?
def inorder(root):
    """Prints the BST in ascending order."""
    if root:
        inorder(root.left)
        print(f"Name: {root.first_name} {root.second_name}.\nPhone number: {root.phone_nr}")
        inorder(root.right)

def assign_row(current: Node, row: int = 0) -> None:
    current.row = row

    if current.left != None:
        assign_row(current.left, row + 1)

    if current.right != None:
        assign_row(current.right, row + 1)

        
def to_list(node: Node):

    node_list = [node]

    if node.left != None:
        node_list = to_list(node.left) + node_list

    if node.right != None:
        node_list = node_list + to_list(node.right)

    return node_list

def assign_cols(node_list: List[Node]):
    for idx, node in enumerate(node_list):
        node.col = idx

def print_tree(root: Node):
    assign_row(root)
    sorted_nodes = to_list(root)
    assign_cols(sorted_nodes)

    node_table = [[]]

    for node in sorted_nodes:
        row = list_get(node_table, node.row, [])
        if row == None:
            row = []

        set_with_fill(row, node, node.col)
        set_with_fill(node_table, row, node.row)

    for row in node_table:
        for col in row:
            if col is None:
                print("     ", end='')
            else:
                print(col.first_name, end='')
        print()


def min_value_node(node):
    """Finds the node with the smallest value from current node"""
    current = node

    #loop down to find the leftmost leaf.
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

    #If the name to be deleted is greater than the
    #root's first name. Then search right side of BST
    elif first_name > root.first_name:
        root.right = delete_node(root.right, first_name)

    #If first name is the same as root, then this is the node.
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
        
        #Copy temp node to destination node
        root.first_name = temp.first_name
        root.second_name = temp.second_name
        root.phone_nr = temp.phone_nr

        #Delete the inorder successor.
        root.right = delete_node(root.right, temp.first_name)

    return root

""" def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i) """
 
 
""" # Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return "NULL"
    if level == 1:
        print(root.first_name, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
 
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1 """
 

#For resting purposes
def main():
    #         Pappa
    #       /      \
    #     Arman     Xena
    #    /   \     /   \
    # None  None None   Zebra
    
  

    r = Node("Pappa", "Efternamn", 12345)
    r = insert(r, "Arman", "Iqbal", 7654321)
    r = insert(r, "Xena", "Princess", 1726758)
    r = insert(r, "Zebra", "Svenson", 771628)
    r = insert(r, "Abba", "AB", 161514514)
    r = insert(r, "Katy", "AB", 161514)   
    r = insert(r, "Rashid", "Waraich", 1875718)
    r = insert (r, "ZZ-----", "Top", 111)

    inorder(r)
    print("\n")

    print_tree(r)




if __name__ == "__main__":
    main()