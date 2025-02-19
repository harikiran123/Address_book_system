from loggers import logger


class Add_multiple:

    def __init__(self,address_book):

        '''
        Description:To in create a new empty list and new instance to add the the multiple address in to the main list in one push
        parameter:address_book
        return:None
        '''

        logger.info("initilizing Add_ multiple class")
        self.multiple_contacts=[]
        self.Valide=address_book
        
    def add_contact(self):

        '''
        Description:collecting the multiple address and add them  to the main list
        parameter:None
        return:None 
        '''

        logger.info("adding multiple contacts")
        no_of_contacts = int(input("ente the how many contacts you need to enter : "))
        for i in range (no_of_contacts):
            first_name=input("enter the first name : ")
            last_name = input("enter the last name : ")
            address = input("enter the address : ")
            zip = self.Valide.validate_zip()
            phone_number=self.Valide.validate_phone()
            mail=input("enter the mail : ")
            contact ={'first_name': first_name,'last_name': last_name,'address': address,'zip':zip,'phone_number':phone_number,'mail':mail }
            self.multiple_contacts.append(contact)
            logger.info(f"address added:{contact}")
            print("\n address added successfully ")
        self.Valide.contacts.extend(self.multiple_contacts)
        logger.info("seccess fully multiple address to the main list")
        print("\n successfully added to the main list")
   
class address_book_info:

    def __init__(self):

        '''
        Description: create a empty list
        parameters:None
        return:None
        '''
        logger.info("intilizing address_book_info")
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
                logger.info(f"valid zip:{zip}")
                return zip
            else:
                logger.warning("invalid zip")
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
                logger.info(f"valid zip : {phone}")
                return phone
            else:
                logger.warning("invalid phone number")
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
        logger.info(f"address added:{contact}")
        print("\n added contact successfully")

    def display(self):

        '''
        Description:To print the people in the address book
        parameters:None
        return:None
        '''

        if not self.contacts:
            logger.info("no contact in the address book")
            print("no people in the address book")
        else:
            logger.info("displaying contacts")
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
                    logger.info(f"editing contact info of {self.contacts[i]}")
                    print("\nContact found. You can edit the details now.")
                    while True:
                        print("\nAvailable keys: first_name, last_name, address, zip, phone_number, mail")
                        key = input("Enter the key you need to edit (or type 'exit' to stop editing): ").strip().lower()
                        if key == 'exit':
                            print("Editing completed.\n")
                            return
                        elif key in self.contacts[i]:
                            if key == 'zip':
                                logger.info("editing completed")
                                new_value = self.validate_zip()
                            elif key == 'phone_number':
                                new_value = self.validate_phone()
                            else:
                                new_value = input(f"Enter new value for {key}: ")

                            self.contacts[i][key] = new_value
                            logger.info(f"updated {key}:{new_value}")
                            print(f"{key} updated successfully.")

                        else:
                            logger.warning(f"invalid {key}")
                            print("Invalid key. Try again.")
                            continue
            else:
               logger.info("contact not found for editing")
               print("Contact not found Try again")
               continue
    
    def delete_address(self):

        '''
        Descrption:to delete the existing user from the address book
        parameter:None
        return:None
        '''

        while True:
            first=input("enter the fist name to delete : ")
            last=input("enter the last name to delete : ")
            for i in range (len(self.contacts)):
                if self.contacts[i]['first_name'] == first and self.contacts[i]['last_name']==last:
                    logger.info(f"deletin contact:{self.contacts[i]}")
                    del self.contacts[i]
                    print("\nsuccessfully deleted the address")
                    return
            else:
               logger.warning("contact not found to delete")
               print("contact not found  try again")
               continue

class Address_book:

    def __init__(self):

        '''
        Description:calling the main class
        parameter:None
        return:None
        '''

        logger.info("initializing Address_book class")
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
            print("5 to delete the address")
            print("6 to add multiple address")
            value= input(" \nenter the value : ")
            if value == '1':
                logger.info("user chosen to add the address")
                self.address_book.add_contact()
            elif value == '2':
                logger.info("user chosen to dispaly the address")
                self.address_book.display()
            elif value == '3':
                logger.info("user chosen to exit the program")
                print("exiting program..")
                break
            elif value == '4':
                logger.info("user chosen to edit the address")
                self.address_book.edit_details()
            elif value == '5':
                logger.info("user chosen to delete the address")
                self.address_book.delete_address()
            elif value == '6':
                logger.info("user chosen to add multiple address")
                self.add_multiple=Add_multiple(self.address_book)
                self.add_multiple.add_contact()
            else:
                print("invalid number")


if __name__ =='__main__':
    Address_book().main()  


