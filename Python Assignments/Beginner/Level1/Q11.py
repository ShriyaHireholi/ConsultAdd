def sum_of_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
        
    return num

def main():
    user_input = int(input("Enter num to find sum of its digits: "))
    ans = sum_of_digits(user_input)
    print(f"Output: {ans}")

if __name__ == "__main__":
    main()
