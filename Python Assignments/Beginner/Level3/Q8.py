def parse_string(s):
    string = s.replace('0', ' ').split()
    ans = {'first_name': string[0], 'last_name': string[1], 'id': string[2]}
    return ans

def main():
    user_input1 = input("Enter encoded string: ")
    ans = parse_string(user_input1)
    print(f"Result: {ans}")

if __name__ == "__main__":
    main()
