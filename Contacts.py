contacts = {}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, details in contacts.items():
                print(name, "-", details["Phone"])

    # Search Contact
    elif choice == "3":
        search = input("Enter Name or Phone Number: ")

        found = False
        for name, details in contacts.items():
            if search == name or search == details["Phone"]:
                print("\nContact Found")
                print("Name:", name)
                print("Phone:", details["Phone"])
                print("Email:", details["Email"])
                print("Address:", details["Address"])
                found = True
                break

        if not found:
            print("Contact not found.")

    # Update Contact
    elif choice == "4":
        name = input("Enter Name to Update: ")

        if name in contacts:
            contacts[name]["Phone"] = input("Enter New Phone: ")
            contacts[name]["Email"] = input("Enter New Email: ")
            contacts[name]["Address"] = input("Enter New Address: ")
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    # Delete Contact
    elif choice == "5":
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    # Exit
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")
