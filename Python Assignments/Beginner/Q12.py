def reverse_number(num):
    return num[::-1]

def main():
    user_input = input("Enter num to find sum of its digits: ")
    ans = reverse_number(user_input)
    print(f"Output: {ans}")

if __name__ == "__main__":
    main()
