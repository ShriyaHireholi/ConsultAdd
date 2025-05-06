def run_length(s):
    if not s:
        return ''
    
    result = ''
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result

def main():
    user_input1 = input("Enter encoded string: ")
    ans = run_length(user_input1)
    print(f"Result: {ans}")

if __name__ == "__main__":
    main()
