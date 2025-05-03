def reverse_string(s):
    lst = s.split()
    lst = lst[::-1]
    return s[::-1]

def main():
    user_input = input("Enter string to be reversed: ")
    ans = reverse_string(user_input)
    print(f"Output After Reverse: {ans}")

if __name__ == "__main__":
    main()
