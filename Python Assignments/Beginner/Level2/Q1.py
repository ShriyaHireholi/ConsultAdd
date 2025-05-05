def count_freq(l1, l2):
    common = list(set(l1) & set(l2))
    return common

def main():
    user_input1 = input("Enter numbers separated by space for 1st list: ")
    num_list1 = [int(x) for x in user_input1.split()]
    user_input2 = input("Enter numbers separated by space for 2nd list: ")
    num_list2 = [int(x) for x in user_input2.split()]
    ans = count_freq(num_list1, num_list2)
    print(f"Common numbers: {ans}")

if __name__ == "__main__":
    main()
