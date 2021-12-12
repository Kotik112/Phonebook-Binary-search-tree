# TODO 
# 1. Self balancing tree.

from bst import Node, delete_node, search, insert, inorder, print_tree
from phonebook import phonebook_input, name_input, main_menu, read_file

def main():

    loop = True
    bst: Node = None
    
    while (loop):
        main_menu()
        menu_choice = int(input("\nEnter your choice (1-6): "))
        #Add a new entry to the BST.
        if menu_choice == 1:
            first_name, second_name, phone_nr = phonebook_input()
            bst = insert(bst, first_name, second_name, phone_nr)
            

        #Search for a keyword in the BST.
        elif menu_choice == 2: 
            name = name_input()
            node = search(bst, name)
            print(node)
            

        #Print the BST in ascending order.
        elif menu_choice == 3:
            inorder(bst)
            
        #Print the BST in tree form.
        elif menu_choice == 4:
            print_tree(bst)

        #Delete a node from the BST. VG
        elif menu_choice == 5:
            name = name_input()
            delete_node(bst, name)
            print(bst)
        
        #Read from file.
        elif menu_choice == 6:
            print("Reading file...")
            bst = read_file("data.txt") 
            
        
        #Exit program.
        elif menu_choice == 7:
            print("Exiting phonebook.")
            loop = False
            

        #Invalid choice.
        else:
            print("Invalid choice. Your options are 1-6.")
        
if __name__ == "__main__":
    try:
        main()

    except ValueError as e:
        print(e)