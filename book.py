def user_details():

    """
    Description: Collects user details like name, address, city, state, zip, phone number, and email.
    Parameter: None
    Return: Dictionary containing user details.
    """

    user_info = {
        "First Name": input("Enter the first name: "),
        "Last Name": input("Enter the last name: "),
        "Address": input("Enter the address: "),
        "City": input("Enter the city: "),
        "State": input("Enter the state: "),
        "Zip": input("Enter the city zip: "),
        "Phone Number": int(input("Enter the phone number: ")),
        "Email": input("Enter the email: ")
    }
    return user_info

def main():

    """
    Description:prints the user details 
    Parameter: None
    Return: None
    """

    user_info = user_details()
    print("\nUser Details:")
    for key, value in user_info.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    main()
