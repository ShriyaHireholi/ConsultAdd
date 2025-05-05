def find_median(l1):
    l1.sort()
    n = len(l1)
    mid = n // 2
    if n % 2 == 0:
        return (l1[mid-1] + l1[mid]) / 2
    else:
        return l1[mid]

def main():
    user_input1 = input("Enter temperature separated by space: ")
    num_list1 = [int(x) for x in user_input1.split()]
    ans = find_median(num_list1)
    print(f"\nMedian: {ans:.1f}")

if __name__ == "__main__":
    main()
