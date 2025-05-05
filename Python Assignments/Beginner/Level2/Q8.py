def count_vowels(s):
    cnt = 0
    vowels = 'aeiou'
    for c in s:
        if c in vowels:
            cnt += 1
    return cnt

def main():
    user_input1 = input("Enter string: ")
    ans = count_vowels(user_input1.lower())
    print(f"\nNumber of Vowels: {ans}")

if __name__ == "__main__":
    main()
