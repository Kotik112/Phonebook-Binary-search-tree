from bst import Node, insert

def phonebook_input():
    """Takes input for the phone book entry."""
    #input for first name
    first_name = input("Enter the first name: ")
    if first_name.isdigit():
        raise ValueError("The first name cannot be numeric.")
    first_name = first_name.lower().capitalize()

    #Input for second name
    second_name = input("Enter the surname: ")
    if second_name.isdigit():
        raise ValueError("The second name cannot be numeric.")
    second_name = second_name.lower().capitalize()

    #Input for phone number
    phone_nr = input("Enter the phone number: ")
    if phone_nr.islower() or phone_nr.isalpha():
        raise ValueError("The telephone number must be numeric.")
    phone_nr = int(phone_nr)

    #Return all input
    return first_name, second_name, phone_nr

def name_input():
    #input for first name
    first_name = input("Enter the first name: ")
    if not first_name:
        raise(ValueError("Empty string."))
        
    #If input is numerical.
    if first_name.isdigit():
        raise ValueError("The first name cannot be numeric.")
    first_name = first_name.lower().capitalize()

    return first_name

def main_menu():
    print("*"*10 + " Main Menu " + "*"*10)
    print("""
    1.   Add a new entry into the phonebook.
    2.   Search for an entry in the phonebook.
    3.   Print all entries in ascending order.
    4.   Print the phonebook in tree form.
    5.   Delete an entry from phonebook.
    6.   Read from file.
    7.   Exit program.""")

def read_file(filename) -> Node:
    """Read File"""
    f = open(filename, "r")
    if f == None:
        raise ValueError(f"Could not open {filename}.")

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

    f.close()
    return bst

