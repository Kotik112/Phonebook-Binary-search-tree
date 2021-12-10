#TODO 
# 1. Delete. 
# 2. Self balancing tree.
# 3. Read from file

from bst import Node, delete_node, search, insert, inorder
from io_phonebook import phonebook_input, name_input, main_menu, read_file

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
            

        #Delete a node from the BST. VG
        elif menu_choice == 4:
            name = name_input()
            delete_node(bst, name)
            print(bst)
            

        #Read from file.
        elif menu_choice == 5:
            print("TODO: Read file")
            #read_file("data.txt") 
            
        
        #Exit program.
        elif menu_choice == 6:
            print("Exiting phonebook.")
            loop = False
            

        #Invalid choice.
        else:
            print("Invalid choice. Your options are 1-6.")
        
main()   