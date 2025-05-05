import Password_checker_function

"""it takes the input from the user and check the password"""
print("\n----------INSTRUCTIONS----------\n")
print("* Your Password Should be length of 7 or more Charactor,"
      "\n* It should contain at least one number, "
      "\n* One capital letter and one small letter\n")
user_input = input("Enter your password: ")
check = Password_checker_function.password_checker(user_input)

if check == "Week":
    print(f"your password is checked as {check}.")
    while True:
        print("* Please read the instruction carefully and try again\n")
        user_input = input("Enter your password again: ")
        check = Password_checker_function.password_checker(user_input)
        if check == "Strong":
            break
else:
    print(f"your password is checked as {check}.")