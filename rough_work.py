while True:
    input_name = input("Enter your name : ")
    if input_name == "q" or input_name == "Q":
        break
    input_phone_number = input("Enter your phone number : ")

    with open ("/Users/anuragpareek/Desktop/ListOfNameAndPhoneNumber.txt","a") as file_object:
        file_object.write(f"{input_name.upper().ljust(20,'.')}{input_phone_number.upper().rjust(20,' ')}\n")
    