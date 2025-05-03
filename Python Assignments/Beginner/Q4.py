def sum_of_odd_nums(start, stop):
    total = 0
    for num in range(start, stop+1):
        if num%2 != 0:
            total += num
    return total

def main():
    print("Enter starting and stopping points")
    start = int(input("Start: "))
    stop = int(input("Stop: "))

    sum_of_numbers = sum_of_odd_nums(start, stop)
    print(f"\nSum: {sum_of_numbers}")

if __name__ == "__main__":
    main()