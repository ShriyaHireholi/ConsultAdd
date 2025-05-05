def login_page():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for _ in range(3):
        re_type = input("\nRe-type your password: ")
        if re_type == password:
            print("Password is correct")
            return
        else:
            print("Password is incorrect")

    print("\nExceeded maximum attempts.")
    return

def main():
    login_page()

if __name__ == "__main__":
    main()
