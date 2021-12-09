#TODO 
# 1. Delete and rearrange tree.
# 2. Self balancing tree.
# 3. Read from file

from bst import Node, delete_node, search, insert, inorder
from io_phonebook import phonebook_input, name_input, main_menu
#from menu_enum import Menu

#### FOR TESTING PURPOSES
r = Node("Pappa", "Efternamn", 12345)
r = insert(r, "Arman", "Iqbal", 7654321)
r = insert(r, "Xena", "Princess", 1726758)
r = insert(r, "Zebra", "Svenson", 771628)
r = insert(r, "Jan", "Lepedus", 917581)
inorder(r)
#### END TEST


def main():
    loop = True
    bst: Node ####
    main_menu()
    menu_choice = int(input("\nEnter your choice (1-6): "))
    while (loop):
        #Add a new entry to the BST.
        if menu_choice == 1:
            first_name, second_name, phone_nr = phonebook_input()
            bst = insert(bst, first_name, second_name, phone_nr)
            break

        #Search for a keyword in the BST.
        elif menu_choice == 2: 
            name = name_input()
            node = search(bst, name)
            print(node)
            break

        #Print the BST in ascending order.
        elif menu_choice == 3:
            inorder(bst)
            break

        #Delete a node from the BST. VG
        elif menu_choice == 4:
            name = name_input()
            delete_node(r, name)
            print(r)
            break

        #Read from file.
        elif menu_choice == 5:
            print("TODO: Read file") 
            break
        
        #Exit program.
        elif menu_choice == 6:
            print("Exiting phonebook.")
            loop = False
            break

        #Invalid choice.
        else:
            print("Invalid choice. Your options are 1-6.")
        
main()   