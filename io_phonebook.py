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
    if phone_nr.islower() or phone_nr.isalpha() or phone_nr.isalnum():
        print("THe telephone number must be numeric.")
        return None
    phone_nr = int(phone_nr)

    #Return all input
    return first_name, second_name, phone_nr

def main_menu():
    print("*"*10 + " Main Menu " + "*"*10 + "\n")
    print("1.   Add a new entry into the BST phonebook.")
    print("2.   Search for an entry.")
    print("3.   Print all entries.")
    print("4.   (VG) Delete an entry from BST.")
    print("5.   Exit program.")
    