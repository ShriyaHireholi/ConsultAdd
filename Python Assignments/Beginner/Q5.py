def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    num = int(input("Enter a number to find its factorial: "))
    
    if num < 0:
        print("\nFactorial is not defined for negative numbers.")
    else:
        fact = factorial(num)
        print(f"\nFactorial of {num} is {fact}")

if __name__ == "__main__":
    main()
