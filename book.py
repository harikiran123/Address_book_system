from loggers import logger
import os
import csv
import json

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
        state = input("Enter the state: ")

        contact = {
            'first_name': first_name,
            'last_name': last_name,
            'address': address,
            'zip': zip_code,
            'phone_number': phone_number,
            'mail': mail,
            'city': city,
            'state': state
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
        matching_contacts = []
        for contact in self.contacts:
            if contact.get('city', '').lower() == city.lower():
                matching_contacts.append(contact)
        return matching_contacts

    def search_by_state(self, state):

        '''
        Description: Search for contacts by state name.
        Parameters: state (str)
        Return: List of contacts in the specified state.
        '''

        logger.info(f"Searching contacts in state: {state}")
        matching_contacts = []
        for contact in self.contacts:
            if contact.get('state', '').lower() == state.lower():
                matching_contacts.append(contact)
        return matching_contacts

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
                        print("\nAvailable keys: first_name, last_name, address, zip, phone_number, mail, city, state")
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

    def sort_contacts_by_name(self):

        '''
        Description: Sort contacts alphabetically by first name.
        Parameters: None
        Return: None
        '''

        logger.info("Sorting contacts by name.")
        self.contacts.sort(key=lambda x: x['first_name'].lower())
        print("\nContacts sorted by name successfully.")
        self.display_contacts()

    def sort_contacts_by_state(self):

        '''
        Description: Sort contacts alphabetically by state .
        Parameters: None
        Return: None
        '''

        logger.info("Sorting contacts by state.")
        self.contacts.sort(key=lambda x: x['state'].lower())
        print("\nContacts sorted by state successfully.")
        self.display_contacts()


class Address_Book_Manager:

    def __init__(self):

        """
        Description: Initialize an empty dictionary for storing multiple address books.
        Parameters: None
        Return: None
        """

        logger.info("Initializing Address_Book_Manager")
        self.address_books = {}
        self.filename = "address_book.json"  
        self.load_from_json()  

    def save_to_json(self):

        """
        Description: Write the address book data into a JSON file.
        Parameters: None
        Return: None
        """

        try:
            data = {name: book.contacts for name, book in self.address_books.items()}

            with open("address_book.json", "w") as file:
                json.dump(data, file, indent=4)

            logger.info("Address book saved successfully to JSON.")
            print("Address book saved successfully to JSON.")
        except Exception as e:
            logger.warning(f"Error saving to JSON: {e}")
            print(f"Error saving to JSON: {e}")

    def load_from_json(self):

        """
        Description: Read the address book data from a JSON file.
        Parameters: None
        Return: None
        """
        
        try:
            if not os.path.exists("address_book.json"):
                print("No previous address book found, starting fresh.")
                return

            with open("address_book.json", "r") as file:
                data = json.load(file)

            self.address_books.clear()
            for book_name, contacts in data.items():
                self.address_books[book_name] = Address_Book_Info(book_name)
                self.address_books[book_name].contacts = contacts

            print("Address book loaded successfully from JSON.")
        except Exception as e:
            print(f"Error loading JSON file: {e}")


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

    def search_person_with_state(self):

        '''
        Description: Search for a person by state across all address books.
        Parameters: None
        Return: None
        '''

        if not self.address_books:
            print("No address books available. Create one first.")
            return

        state = input("Enter the state name: ").strip()
        if not state:
            print("Invalid input. Please enter a valid state.")
            return

        results = []
        for book_name, book in self.address_books.items():
            matches = book.search_by_state(state)
            for contact in matches:
                contact_info = {**contact, 'Address Book': book_name}
                results.append(contact_info)

        if results:
            print("\nSearch Results:")
            for i, contact in enumerate(results, start=1):
                print(f"{i}. {contact}")
        else:
            print(f"No contacts found in state '{state}'.")

    def search_person_city_state(self):

        '''
        Description: Search for a person by city or state across all address books.
        Parameters: None
        Return: None
        '''

        if not self.address_books:
            print("No address books available. Create one first.")
            return

        search_query = input("Enter the city or state to search: ").strip().lower()
        if not search_query:
            print("Invalid input. Please enter a valid city or state.")
            return

        results = []
        for book_name, book in self.address_books.items():
            city_matches = book.search_by_city(search_query)
            for contact in city_matches:
                contact_info = {**contact, 'Address Book': book_name}
                results.append(contact_info)

            state_matches = book.search_by_state(search_query)
            for contact in state_matches:
                contact_info = {**contact, 'Address Book': book_name}
                results.append(contact_info)

        unique_results = []
        seen_contacts = set()
        for contact in results:
            contact_id = f"{contact['first_name']}_{contact['last_name']}"
            if contact_id not in seen_contacts:
                unique_results.append(contact)
                seen_contacts.add(contact_id)

        if unique_results:
            print("\nSearch Results:")
            for i, contact in enumerate(unique_results, start=1):
                print(f"{i}. {contact}")
        else:
            print(f"No contacts found in '{search_query}'.")
        print(f"total count is : {len(unique_results)}")

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
            print("9. Search person by state across all address books")
            print("10. Search person by city or state across all address books")
            print("11. Sort contacts by name in an address book")
            print("12. sort contact by state in the address book")
            print("13. Save address book to json")
            print("14. Load address book from json")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_address_book()
            elif choice in {'2', '3', '4', '5', '6', '11','12'}:
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
                    elif choice == '11':
                        book.sort_contacts_by_name()
                    elif choice == '12':
                        book.sort_contacts_by_state()
            elif choice == '7':
                logger.info("User exited the program.")
                print("Exiting program...")
                break
            elif choice == '8':
                self.search_person_across_books()
            elif choice == '9':
                self.search_person_with_state()
            elif choice == '10':
                self.search_person_city_state()
            elif choice == '13':
                self.save_to_json()  
            elif choice == '14':
                self.load_from_json()
            else:
                logger.warning("Invalid choice. Please enter a number between 1 and 11.")
                print("Invalid choice. Try again.")

if __name__ == '__main__':
    Address_Book_Manager().main()