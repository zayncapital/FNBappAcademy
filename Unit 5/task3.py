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
#Call the function
add_contact()

#Display the contact list
print(contacts)