
from bst import Node, insert, inorder #Remove inorder, testing only

def phonebook_input():
    """Takes input for the phone book entry."""
    #input for first name
    first_name = input("Enter the first name: ")
    if first_name.isdigit():
        print("The first name cannot be numeric.")
        return None
    first_name = first_name.lower().capitalize()

    #Input for second name
    second_name = input("Enter the surname: ")
    if second_name.isdigit():
        print("The second name cannot be numeric.")
        return None
    second_name = second_name.lower().capitalize()

    #Input for phone number
    phone_nr = input("Enter the phone number: ")
    if phone_nr.islower() or phone_nr.isalpha():
        print("The telephone number must be numeric.")
        return None
    phone_nr = int(phone_nr)

    #Return all input
    return first_name, second_name, phone_nr

def name_input():
    #input for first name
    try:
        first_name = input("Enter the first name: ")
        if not first_name:
            raise(ValueError("Empty string."))
    except ValueError as e:
        print(e)
        
    if first_name.isdigit():
        print("The first name cannot be numeric.")
        return None
    first_name = first_name.lower().capitalize()

    return first_name

def main_menu():
    print("*"*10 + " Main Menu " + "*"*10 + "\n")
    print("""1.   Add a new entry into the BST phonebook.")
    2.   Search for an entry.
    3.   Print all entries.
    4.   (VG) Print BST in tree form.
    5.   (VG) Delete an entry from BST.
    6.   Read from file.
    7.   Exit program.""")

def read_file(filename) -> Node:
    """Read File"""
    f = open(filename, "r")
    if f == None:
        print(f"Could not open {filename}.")

    lines = f.readlines()
    names = [] 
    numbers = []
    for i, line in enumerate(lines):
        if i%2 == 0:
            names.append(line)
        if i%2 == 1:
            numbers.append(line)

    bst: Node = None

    for j in range(len(numbers)):
        first_name, second_name = names[j].split(" ")

        #Remove new line from second name and number.
        second_name = second_name.strip("\n")
        numbers[j] = numbers[j].strip("\n")

        #Insert all entries into a binary search tree.
        bst = insert(bst, first_name, second_name, numbers[j])

    #inorder(bst)
    return bst

