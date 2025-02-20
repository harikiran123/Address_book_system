from loggers import logger


class Address_Book_Info:

    def __init__(self):

        '''
        Description: create an empty list.
        Parameters: None
        Return: None
        '''

        logger.info("initializing Address_Book_Info")
        self.contacts = []

    def validate_zip(self):

        '''
        Description: validate the format of the zip code.
        Parameters: None
        Return: None
        '''

        while True:
            zip_code = input("enter the zip: ")
            if zip_code.isdigit():
                logger.info(f"valid zip: {zip_code}")
                return zip_code
            else:
                logger.warning("invalid zip")
                print("error: The input should be an integer")

    def validate_phone(self):

        '''
        Description: Validate the format of the phone number.
        Parameters: None
        Return: None
        '''

        while True:
            phone = input("enter the phone number: ")  
            if phone.isdigit() and len(phone) == 10:
                logger.info(f"valid phone number: {phone}")
                return phone
            else:
                logger.warning("invalid phone number")
                print("error: the phone number should be an integer with exactly 10 digits")

    def add_contact(self):

        '''
        Description: Collect user inputs and add a new contact.
        Parameters: None
        Return: None
        '''

        first_name = input("enter the first name: ")
        last_name = input("enter the last name: ")
        address = input("enter the address: ")
        zip_code = self.validate_zip()
        phone_number = self.validate_phone()
        mail = input("enter the email: ")

        contact = {
            'first_name': first_name, 'last_name': last_name, 
            'address': address, 'zip': zip_code, 
            'phone_number': phone_number, 'mail': mail
        }
        self.contacts.append(contact)
        logger.info(f"Address added: {contact}")
        print("\nContact added successfully")

    def display_contacts(self):

        '''
        Description: Display all contacts in the address book.
        Parameters: None
        Return: None
        '''

        if not self.contacts:
            logger.info("no contacts in the address book")
            print("no contacts in the address book.")
        else:
            logger.info("displaying contacts")
            print("\naddress Book Contacts:")
            for contact in self.contacts:
                print(contact)

    def edit_contact(self):

        '''
        Description: Edit a contact's details.
        Parameters: None
        Return: None
        '''

        while True:
            first = input("Enter the first name of the contact to edit: ")
            last = input("Enter the last name of the contact to edit: ")

            for contact in self.contacts:
                if contact['first_name'] == first and contact['last_name'] == last:
                    logger.info(f"editing contact info of {contact}")
                    print("contact found you can edit the details now")

                    for key in contact:
                        new_value = input(f"Enter new value for {key} : ")
                        if new_value:
                            contact[key] = new_value

                    logger.info(f"updated contact: {contact}")
                    print("Contact updated successfully.")
                    return  # Exit function once updated
            
            print("contact not found. Please enter valid first and last names.")

    def delete_contact(self):

        '''
        Description: Delete a contact.
        Parameters: None
        Return: None
        '''

        while True:
            first = input("Enter the first name of the contact to delete: ")
            last = input("Enter the last name of the contact to delete: ")

            for contact in self.contacts:
                if contact['first_name'] == first and contact['last_name'] == last:
                    self.contacts.remove(contact)
                    logger.info(f"Deleted contact: {contact}")
                    print("Contact deleted successfully.")
                    return
            
            print("Contact not found. Please enter a valid first and last name.")

    def add_multiple_contacts(self):

        '''
        Description: Add multiple contacts at once.
        Parameters: None
        Return: None
        '''

        count = int(input("Enter the number of contacts to add: "))
        for _ in range(count):
            self.add_contact()


class Address_Book_Manager:
    
    def __init__(self):

        '''
        Description: Maintain a dictionary of multiple address books.
        Parameters: None
        Return: None
        '''

        logger.info("Initializing Address_Book_Manager")
        self.address_books = {}

    def create_address_book(self):

        '''
        Description: Create a new address book with a unique name.
        Parameters: None
        Return: None
        '''

        name = input("Enter the name of the new address book: ")
        if name in self.address_books:
            logger.warning("Address book already exists")
            print("An address book with this name already exists.")
        else:
            self.address_books[name] = Address_Book_Info()
            logger.info(f"Created new address book: {name}")
            print(f"Address book '{name}' created successfully.")

    def select_address_book(self):

        '''
        Description: Select an existing address book with error handling.
        Parameters: None
        Return: None
        '''

        if not self.address_books:
            print("No address books available. Create one first.")
            return None

        print("\nAvailable address books:")
        for book in self.address_books.keys():
            print(f"- {book}")

        while True:
            name = input("Enter the name of the address book: ")
            if name in self.address_books:
                return self.address_books[name]
            print("Address book not found. Please enter a valid name.")

    def main(self):

        '''
        Description: Provide user choices to manage multiple address books.
        Parameters: None
        Return: None
        '''

        while True:
            print("\n1 create a new address book")
            print("2 add a contact to an address book")
            print("3 Display contacts from an address book")
            print("4 edit a contact in an address book")
            print("5 delete a contact from an address book")
            print("6 add multiple contacts to an address book")
            print("7 exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_address_book()
            elif choice in {'2', '3', '4', '5', '6'}:
                book = self.select_address_book()
                if book:
                    if choice == '2':
                        book.add_contact()
                    elif choice == '3':
                        book.display_contacts()
                    elif choice == '4':
                        book.edit_contact()
                    elif choice == '5':
                        book.delete_contact()
                    elif choice == '6':
                        book.add_multiple_contacts()
            elif choice == '7':
                logger.info("user exited the program")
                print("exiting program...")
                break
            else:
                print("invalid choice try again.")


if __name__ == '__main__':
    Address_Book_Manager().main()
