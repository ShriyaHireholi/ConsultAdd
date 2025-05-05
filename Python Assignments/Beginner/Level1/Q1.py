def three_five_both(n):
    if  n % 3 == 0 and n % 5 == 0:
        print("Consultadd - Python Training")
    elif n % 3 == 0:
        print("Consultadd")
    elif n % 5 == 0:
        print("Python Training")

def main():
    num = int(input("Enter a number to check if it is divisible by 3, 5 or both: "))
    three_five_both(num)

if __name__ == "__main__":
    main()