def is_pow_of_two(n):
    if n == 1:
        return True
    if n%2 != 0:
        return False
    return is_pow_of_two(n//2)

def main():
    user_input1 = int(input("Enter number to check if it is pow of 2: "))
    ans = is_pow_of_two(user_input1)
    print(f"\nResult: {ans}")

if __name__ == "__main__":
    main()
