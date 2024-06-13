def get_username(first, last):
    s = first + "." + last
    return s.lower()


def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = get_username(first_name, last_name)
    print("Your username is: " + username)


if __name__ == "__main__":
    main()