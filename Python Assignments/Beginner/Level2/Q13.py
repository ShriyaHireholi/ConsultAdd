def main():
    user_input1 = input("Enter string: ")
    user_input2 = input("Enter char to check: ")
    starts_with = lambda s, w: s.startswith(w)
    ans = starts_with(user_input1, user_input2)
    print(f"\nResult: {ans}")

if __name__ == "__main__":
    main()
