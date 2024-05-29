contact = {} #Empty Dictionary 

#Creating a function to display contact info throught the process.
def DisplayContact(): 
    print()
    for name, number in contact.items(): #Display Dictionary Key and value together. 
        print(f"Name: {name} \t Number: {number}\n")

while True:
    choice = int(input(
        "1. Add new Contact. \n"
        "2. Search Contact \n"
        "3. Display Contact \n"
        "4. Edit Contact \n"
        "5. Delete Contact \n"
        "6. Exit \n"
        "Please input the number between 1-6:  "
    ))

    if choice == 1: #Check if the option is available in choice variable above.
        Name = input("Enter the Name: ")
        Number = input("Enter the Phone Number: ")
        contact[Name] = Number #Way to add contact items to the Dictionary 'Contact'
        
        print("New contact has been added. Please choose an option from  below:\n")

    elif choice == 2:
        SearchContact = input("Please enter the Contact name to see the contact number: ") #check the name first if it's available in the Dictionary
        if SearchContact in contact: #Jodi inputed value are available in contact dictionary
            print(f"{SearchContact}'s Contact number is: {contact[SearchContact]}. Please choose an option from  below:\n ") #Show value by calling the key
        else:
            print("This contact nas was not found!")
    
    elif choice == 3: 
        if not contact:
            print("Contact book is empty! Please choose an option from  below:\n ")
        else:
            DisplayContact()
            print("Please choose an option from  below:\n")

    elif choice == 4: #Edit contact option
        EditContact = input("Please enter the name which number you want to edit: ")
        if EditContact in contact: 
            enterMobile = input("Enter The mobile number to update with: ")
            contact[EditContact] = enterMobile #This is the role to update dictionary items. Dictname[DictKey] =  Value to update.
            print(f"{EditContact}'s phone number has been updated with: {enterMobile}. Please choose an option from  below:\n")
        else:
            print("Sorry, This contact name was not found in our database! Please choose an option from  below:\n")

    elif choice == 5: 
        DeleteContact = input("Which contact you want to delete? Please enter the name: ")
        if DeleteContact not in contact: #check if the inputed name is available in the dictionarly
            print("Error! Please choose an option from  below:\n")
        else:
            contact.pop(DeleteContact) #pop method to delete an dictionry item by calling key
            print(f"{DeleteContact} has been Deleted permanently! Please choose an option from  below:\n")

    elif choice == 6:
        print("You have exit from the program! \n")
        break

    else:
        print("Sorry, you inserted wrong info!")
        break