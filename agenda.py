agenda = []


def get_data_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone: ")
    email = input("Enter the email: ")
    favorite = False
    return {"name": name, "phone": phone, "email": email, "favorite": favorite}


def show_contacts(contacts):
    if not agenda:
        print("No contacts available!")
    else:
        for contact in enumerate(contacts, start=1):
            print(f"{contact}")


while True:
    print("Contact agenda")
    print("1 - Add contact")
    print("2 - Show contacts")
    print("3 - Edit contacts")
    print("4 - Mark/Unmark as favorite")
    print("5 - Show favorites")
    print("6 - Delete contact")
    print("7 - Exit")

    option = input("Choose an option: ")

    if option == "1":
        contact = get_data_contact()
        agenda.append(contact)
        print("Contact added successfully!")
    if option == "2":
        print(agenda)
    elif option == "7":
        break
