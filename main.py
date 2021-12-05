from bst import Node, search, insert, inorder
from io_phonebook import phonebook_input, main_menu
from menu_enum import Menu

def main():
    loop = True
    main_menu()
    menu_choice = input ("\nEnter your choice (1-5): ")
    while (loop):
        match menu_choice:
            case Menu.ADD:
                first_name, second_name, phone_nr = phonebook_input()
                #Insert into root.key here
                bst = insert()

            case Menu.SEARCH:
                pass

            case Menu.PRINT:
                inorder()

            case Menu.DEL:
                pass

            case Menu.EXIT:
                pass
        
    