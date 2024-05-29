contact= {}


def DisplayContact():
    # print("Name \t Number")
    # for name, number in contact.items():
    #     print("{} \t {}".format(name, number))
    file = open("contact-book.txt", "r")
    print(file.read())
    file.close()


while True:
    choice = int(input(
        "1. Add new Contact. \n"
        "2. Search Contact \n"
        "3. Display Contact \n"
        "4. Edit Contact \n"
        "5. Delet Contact \n"
        "6. Exit \n"
        "Please input the number between 1-6: "
    ))

    if choice == 1:
        Name = input("Enter the Name: ")
        Number = input("Enter the Phone Number: ")
        contact[Name] = Number
        
        file = open("contact-book.txt", "a")
        file.write(f"Name: {Name} \t Number: {Number} \n")
     



    elif choice == 2:
        SearchContact = input("Please enter the Contact name: ")
        if Name in SearchContact:
            print(f"{SearchContact} Contact number is: {Number}")
        else:
            print("This nas was not found")

    elif choice == 3:
        DisplayContact()


    else:
        break