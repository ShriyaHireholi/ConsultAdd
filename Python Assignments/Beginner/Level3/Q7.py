def construct_dict(names, subjects):
    ans = {n:s for n, s in zip(names, subjects)}
    return ans

def main():
    user_input1 = input("Enter student names separated by space: ")
    names = [x for x in user_input1.split()]
    user_input2 = input("Enter subjects separated by space: ")
    subjects = [x for x in user_input2.split()]
    ans = construct_dict(names, subjects)
    print(f"Result: {ans}")

if __name__ == "__main__":
    main()
