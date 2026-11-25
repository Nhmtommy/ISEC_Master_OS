def main():

# default user name and password
    name = "admin"
    password = "1234"
# user name and password

    user_name = input("Enter User Name ")
    user_password = input("Enter Password ")
#conditions for user approval to login only if anme and password are both correct
    if user_name == name  and user_password == password:
        print("Login successful")
    elif user_name != name:
        print("User not found")
    elif user_password != password:
        print("Incorrect password")

if __name__ == "__main__":
    main()