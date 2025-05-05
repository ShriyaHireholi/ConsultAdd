def uniq_ele(l1):
    common = list(set(l1))
    return common

def main():
    user_input1 = input("Enter numbers separated by space: ")
    num_list1 = [int(x) for x in user_input1.split()]
    ans = uniq_ele(num_list1)
    print(f"Unique numbers: {ans}")

if __name__ == "__main__":
    main()
