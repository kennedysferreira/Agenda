agenda = []


def get_data_contact(name, phone, email):
    favorite = False
    contact = {"name": name, "phone": phone, "email": email, "favorite": favorite}
    agenda.append(contact)
    print("Contact added successfully!")


def show_contacts(contacts):
    if not agenda:
        print("No contacts available!")
    else:
        for i, contact in enumerate(contacts, start=1):
            contact_name = contact["name"]
            phone = contact["phone"]
            email = contact["email"]
            favorite = contact["favorite"]
            print(f"{i} - Name: {contact_name}, Phone: {phone}, Email: {email}, Favorite: {favorite}")


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
        show_contacts(agenda)
    elif option == "7":
        break
