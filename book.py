class Address_Book_Main:
    def display(self):

        '''
        Description:To print the welcome to address book message
        Parameter:None
        Return:None
        '''

        print("Welcome to address book")

def main():

    """
    Description: To create an instance of Address_Book_Main class and 
    print the welcome message using the display method.
    Parameter: None
    Return: None
    """
    obj = Address_Book_Main()
    obj.display()


if __name__ == '__main__' :
    main()
