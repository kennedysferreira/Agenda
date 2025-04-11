agenda = []


def get_data_contact(name, phone, email):
    favorite = False
    contact = {"name": name, "phone": phone, "email": email, "favorite": favorite}
    agenda.append(contact)
    print("Contact added successfully!")


def check_agenda_empty(agenda):
    if not agenda:
        print("No contacts available!")
        return True
    return False


def show_contacts(contacts):
    if not contacts:
        print("No contacts available!")
    else:
        for i, contact in enumerate(contacts, start=1):
            contact_name = contact["name"]
            phone = contact["phone"]
            email = contact["email"]
            favorite = "Yes" if contact["favorite"] else "No"
            print(
                f"{i} - Name: {contact_name}, Phone: {phone}, Email: {email}, Favorite: {favorite}"
            )


def edit_contact(contacts, contact_index):
    contact = contacts[contact_index]
    new_name = input("Do you want to change the name? (y/n)")
    if new_name.lower() == "y":
        contact["name"] = input("Enter the new name: ")
    else:
        pass
    new_phone = input("Do you want to change the phone? (y/n)")
    if new_phone.lower() == "y":
        contact["phone"] = input("Enter the new phone: ")
    else:
        pass
    new_email = input("Do you want to change the email? (y/n)")
    if new_email.lower() == "y":
        contact["email"] = input("Enter the new email: ")
    else:
        pass
    print("Contact edited successfully!")


while True:
    print("\nContact agenda")
    print("1 - Add contact")
    print("2 - Show contacts")
    print("3 - Edit contacts")
    print("4 - Mark/Unmark as favorite")
    print("5 - Show favorites")
    print("6 - Delete contact")
    print("7 - Exit")

    option = input("Choose an option: ")

    if option == "1":
        name = input("Enter the name: ")
        phone = input("Enter the phone: ")
        email = input("Enter the email: ")
        get_data_contact(name, phone, email)
    elif option == "2":
        if check_agenda_empty(agenda):
            continue
        show_contacts(agenda)
    elif option == "3":
        show_contacts(agenda)
        contact_index = int(input("Enter the contact number: ")) - 1
        edit_contact(agenda, contact_index)
    elif option == "7":
        break
