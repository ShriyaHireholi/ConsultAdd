def perfect_number(n):
    sum_of_divisor = 0
    product_of_divisors = 0
    for i in range(1, n+1):
        if n%i == 0:
            sum_of_divisor += i
            product_of_divisors *= i
    
    if sum_of_divisor == product_of_divisors:
        print("Yes")
    else:
        print("No")

def main():
    num = int(input("Enter a number to find its perfect: "))
    perfect_number(num)

if __name__ == "__main__":
    main()
