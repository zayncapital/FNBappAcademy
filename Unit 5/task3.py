#Creating a Contact book....

contacts = []

def add_contact(): 
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter email address: ")

#Creating a dictionary for the contacts

    contact = {
         "name" : name,
         "phone" : phone,
         "email" : email
    }

#Add it to the list

    contacts.append(contact)

    print ("contact added successfully")

def view_all():
    print("===================")
    print("   ALL CONTACTS")
    print("===================")

    for contact in contacts:
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("-------------------")

def search_contact():
    search_name = input("Enter contact name: ")

    for contact in contacts:
        if contact["name"] == search_name:
            print(f"Name : {contact['name']}")
            print(f"Phone : {contact['phone']}")
            print(f"Email : {contact['email']}")

#Deleting contacts from the contact book...

def delete_contact():
    search_name = input ("Enter the name you want to delete: ")

    for contact in contacts: 
        if contact["name"] == search_name :
            contacts.remove(contact)
            print("Contact removed succesfully!")
            break

#Adding while loop to the contact book. NB: While loop - repeats something while it is true

while True: 
    print("=========================")
    print("     Contact Book")
    print("=========================")
    print("1. Add Contact")
    print("2. Search contact")
    print("3. Delete contacts")
    print("4. view all: ")
    print("5. Exit: ")
    
    choice = input("choose an option: ")
    if choice == "1" : 
        add_contact()
    elif choice == "2" : 
        search_contact()
    elif choice == "3" :
        delete_contact()
    elif choice == "4" : 
        view_all()
    elif choice == "5":
        print("Thank you for using contact Book")
        break
    

    
        
