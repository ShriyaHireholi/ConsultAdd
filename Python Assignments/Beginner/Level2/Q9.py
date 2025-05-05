def err_handle(l1, i):
    try:
        return l1[i]
    except IndexError:
        return "Index Out of Range"

def main():
    user_input1 = int(input("Enter length to create 0-based idx array: "))
    num_list1 = [x for x in range(user_input1)]
    idx = int(input("Enter index you want to access: "))
    ans = err_handle(num_list1, idx)
    print(f"\nResult: {ans}")

if __name__ == "__main__":
    main()
