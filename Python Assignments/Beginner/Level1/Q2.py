def main():
    s = input("Enter a string: ")
    alphabet_cnt = string_cnt = 0
    for c in s:
        if c.isalpha():
            alphabet_cnt += 1
        elif c.isdigit():
            string_cnt += 1
    print(f'Alphabets:{alphabet_cnt} & Numbers:{string_cnt}')


if __name__ == "__main__":
    main()