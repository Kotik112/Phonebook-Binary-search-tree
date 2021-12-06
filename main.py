#TODO 
# 1. Delete and rearrange tree.
# 2. Self balancing tree.

from bst import Node, search, insert, inorder
from io_phonebook import phonebook_input, name_input, main_menu
#from menu_enum import Menu

def main():
    loop = True
    main_menu()
    menu_choice = int(input("\nEnter your choice (1-5): "))
    while (loop):
        if menu_choice == 1:
            #Add a new entry to the BST.
            first_name, second_name, phone_nr = phonebook_input()
            bst = insert(bst, first_name, second_name, phone_nr)

        elif menu_choice == 2:
            #Search for a keyword in the BST.
            name = name_input()
            node = search(name)
            print(node)

        elif menu_choice == 3:
            #Print the BST in ascending order.
            inorder(bst)

        elif menu_choice == 4:
            #Delete a node from the BST.
            pass

        elif menu_choice == 5:
            #Read from file.
            pass

        elif menu_choice == 6:
            #Exit program
            raise(SystemExit)
        
main()   