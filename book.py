class address_book_info:

    def __init__(self):

        '''
        Description: create a empty list
        parameters:None
        return:None
        '''

        self.contacts =[]
    
    def validate_zip(self):

        '''
        Description:To check the formate of zip
        parameters:None
        return:zip
        '''

        while True:
            zip=input("enter the zip : ")
            if zip.isdigit():
                return zip
            else:
                print("error: the input should be in integer")
                continue
                
    def validate_phone(self):

        '''
        Description:to check the formate of phone number
        parametersa:None
        return:phone_number
        '''

        while True:
            phone =input("enter the phone number : ")  
            if phone.isdigit() and len(phone) == 10:
                return phone
            else:
                print("error the phone number should be in integer and atlest 10 ")   
            
    def add_contact(self):

        '''
        Description:Take the user inputs
        parameters:None
        return:None
        '''

        first_name = input("enter the first name : ")
        last_name = input("enter the lasat name : ")
        address = input("enter the address : ")
        zip = self.validate_zip()
        phone_number = self.validate_phone()
        mail = input("enter the mail : ")
        
        contact = {'first_name': first_name,'last_name': last_name,'address': address,'zip':zip,'phone_number':phone_number,'mail':mail }
        self.contacts.append(contact)
        print("\n added contact successfully")

    def display(self):

        '''
        Description:To print the people in the address book
        parameters:None
        return:None
        '''

        if not self.contacts:
            print("no people in the address book")
        else:
            print("address book contacts")
            for i in self.contacts:
                print(i)

    def edit_details(self): 

          '''
          Description: To edit the address book details using the first and last name
          parameters:None
          retrun:None
          ''' 

          while True:
            first = input("Enter the first name you want to edit: ")
            last = input("Enter the last name you want to edit: ")
            for i in range(len(self.contacts)):
                if self.contacts[i]['first_name'] == first and self.contacts[i]['last_name'] == last:
                    print("\nContact found. You can edit the details now.")
                    while True:
                        print("\nAvailable keys: first_name, last_name, address, zip, phone_number, mail")
                        key = input("Enter the key you need to edit (or type 'exit' to stop editing): ").strip().lower()
                        if key == 'exit':
                            print("Editing completed.\n")
                            return
                        elif key in self.contacts[i]:
                            if key == 'zip':
                                new_value = self.validate_zip()
                            elif key == 'phone_number':
                                new_value = self.validate_phone()
                            else:
                                new_value = input(f"Enter new value for {key}: ")

                            self.contacts[i][key] = new_value
                            print(f"{key} updated successfully.")

                        else:
                            print("Invalid key. Try again.")
                            continue
                else:
                  print("Contact not found. Try again.")
                  continue

class Address_book:

    def __init__(self):

        '''
        Description:calling the main class
        parameter:None
        return:None
        '''

        self.address_book = address_book_info()
    
    def main(self):

        '''
        Description:using user choise to execute the program
        parameter:None
        return:None
        '''
        
        while True:
            print("1 to add contact")
            print("2 to display contact")
            print("3 to exit contact")
            print("4 to edit existing user")
            value= input(" \nenter the value : ")
            if value == '1':
                self.address_book.add_contact()
            elif value == '2':
                self.address_book.display()
            elif value == '3':
                print("exiting program..")
                break
            elif value == '4':
                self.address_book.edit_details()

            else:
                print("invalid number")


if __name__ =='__main__':
    Address_book().main()  


