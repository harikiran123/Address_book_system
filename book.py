from loggers import logger


class Address_Book_Info:
    def __init__(self, address_book_name):
        '''
        Description: Initialize an empty contact list.
        Parameters: address_book_name (str) - Name of the address book.
        Return: None
        '''
        logger.info("Initializing Address_Book_Info")
        self.contacts = []
        self.address_book_name = address_book_name

    def validate_zip(self):
        '''
        Description: Validate the format of the zip code.
        Parameters: None
        Return: Validated zip code (str)
        '''
        while True:
            zip_code = input("Enter the zip: ")
            if zip_code.isdigit():
                logger.info(f"Valid zip: {zip_code}")
                return zip_code
            else:
                logger.warning("Invalid zip")
                print("Error: The input should be an integer.")

    def validate_phone(self):
        '''
        Description: Validate the format of the phone number.
        Parameters: None
        Return: Validated phone number (str)
        '''
        while True:
            phone = input("Enter the phone number: ")
            if phone.isdigit() and len(phone) == 10:
                logger.info(f"Valid phone number: {phone}")
                return phone
            else:
                logger.warning("Invalid phone number")
                print("Error: The phone number should be an integer with exactly 10 digits.")

    def add_contact(self):
        '''
        Description: Add a new contact to the address book.
        Parameters: None
        Return: None
        '''
        while True:
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")

            # Check for duplicate contacts
            if any(contact['first_name'] == first_name and contact['last_name'] == last_name for contact in self.contacts):
                logger.warning(f"Duplicate contact found: {first_name} {last_name}")
                print(f"Error: Contact {first_name} {last_name} already exists. Try with another name.")
            else:
                break

        address = input("Enter the address: ")
        zip_code = self.validate_zip()
        phone_number = self.validate_phone()
        mail = input("Enter the email: ")
        city = input("Enter the city: ")

        contact = {
            'first_name': first_name,
            'last_name': last_name,
            'address': address,
            'zip': zip_code,
            'phone_number': phone_number,
            'mail': mail,
            'city': city
        }
        self.contacts.append(contact)
        logger.info(f"Contact added: {contact}")
        print("\nContact added successfully.")

    def search_by_city(self, city):
        '''
        Description: Search for contacts by city name.
        Parameters: city (str)
        Return: List of contacts in the specified city.
        '''
        logger.info(f"Searching contacts in city: {city}")
        return [contact for contact in self.contacts if contact.get('city', '').lower() == city.lower()]

    def display_contacts(self):
        '''
        Description: Display all contacts in the address book.
        Parameters: None
        Return: None
        '''
        if not self.contacts:
            logger.info("No contacts in the address book.")
            print("No contacts in the address book.")
        else:
            logger.info("Displaying contacts.")
            print("\nAddress Book Contacts:")
            for contact in self.contacts:
                print(contact)

    def edit_details(self):
        '''
        Description: Edit the details of a contact using the first and last name.
        Parameters: None
        Return: None
        '''
        while True:
            first = input("Enter the first name of the contact to edit: ")
            last = input("Enter the last name of the contact to edit: ")

            for contact in self.contacts:
                if contact['first_name'] == first and contact['last_name'] == last:
                    print("\nContact found. You can edit the details now.")
                    while True:
                        print("\nAvailable keys: first_name, last_name, address, zip, phone_number, mail, city")
                        key = input("Enter the key you need to edit (or type 'exit' to stop editing): ").strip().lower()
                        if key == 'exit':
                            print("Editing completed.\n")
                            return
                        elif key in contact:
                            if key == 'zip':
                                new_value = self.validate_zip()
                            elif key == 'phone_number':
                                new_value = self.validate_phone()
                            else:
                                new_value = input(f"Enter new value for {key}: ")

                            contact[key] = new_value
                            print(f"{key} updated successfully.")
                        else:
                            print("Invalid key. Try again.")
                    return
            else:
                print("Contact not found. Try again.")

    def delete_contact(self):
        '''
        Description: Delete an existing contact from the address book.
        Parameters: None
        Return: None
        '''
        while True:
            first = input("Enter the first name of the contact to delete: ")
            last = input("Enter the last name of the contact to delete: ")

            for i, contact in enumerate(self.contacts):
                if contact['first_name'] == first and contact['last_name'] == last:
                    del self.contacts[i]
                    logger.info(f"Contact deleted: {first} {last}")
                    print("\nContact deleted successfully.")
                    return
            else:
                print("Contact not found. Try again.")

    def add_multiple_contacts(self):
        '''
        Description: Add multiple contacts to the address book.
        Parameters: None
        Return: None
        '''
        logger.info("Adding multiple contacts.")
        no_of_contacts = int(input("Enter how many contacts you need to add: "))
        for _ in range(no_of_contacts):
            self.add_contact()
        logger.info("Successfully added multiple contacts.")


class Address_Book_Manager:
    def __init__(self):
        '''
        Description: Initialize an empty dictionary for storing multiple address books.
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
            logger.warning("Address book already exists.")
            print("An address book with this name already exists.")
        else:
            self.address_books[name] = Address_Book_Info(name)
            logger.info(f"Created new address book: {name}")
            print(f"Address book '{name}' created successfully.")

    def select_address_book(self):
        '''
        Description: Select an existing address book.
        Parameters: None
        Return: Selected Address_Book_Info object or None
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

    def search_person_across_books(self):
        '''
        Description: Search for a person by city across all address books.
        Parameters: None
        Return: None
        '''
        if not self.address_books:
            print("No address books available. Create one first.")
            return

        city = input("Enter the city name: ").strip()
        if not city:
            print("Invalid input. Please enter a valid city.")
            return

        results = []
        for book_name, book in self.address_books.items():
            matches = book.search_by_city(city)
            for contact in matches:
                contact_info = {**contact, 'Address Book': book_name}
                results.append(contact_info)

        if results:
            print("\nSearch Results:")
            for i, contact in enumerate(results, start=1):
                print(f"{i}. {contact}")
        else:
            print(f"No contacts found in city '{city}'.")

    def main(self):
        '''
        Description: Provide user choices to manage multiple address books.
        Parameters: None
        Return: None
        '''
        while True:
            print("\n1. Create a new address book")
            print("2. Add a contact to an address book")
            print("3. Display contacts from an address book")
            print("4. Edit a contact in an address book")
            print("5. Delete a contact from an address book")
            print("6. Add multiple contacts to an address book")
            print("7. Exit")
            print("8. Search person by city across all address books")

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
                        book.edit_details()
                    elif choice == '5':
                        book.delete_contact()
                    elif choice == '6':
                        book.add_multiple_contacts()
            elif choice == '7':
                logger.info("User exited the program.")
                print("Exiting program...")
                break
            elif choice == '8':
                self.search_person_across_books()
            else:
                print("Invalid choice. Try again.")


if __name__ == '__main__':
    Address_Book_Manager().main()