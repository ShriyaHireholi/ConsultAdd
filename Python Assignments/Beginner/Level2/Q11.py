def string_list(s):
    a = []
    for w in s:
        a.append(w)
    return a

def main():
    user_input1 = input("Enter string separated by space: ").split()
    ans = list(map(string_list, user_input1))
    print(f"\nResult: {ans}")

if __name__ == "__main__":
    main()
