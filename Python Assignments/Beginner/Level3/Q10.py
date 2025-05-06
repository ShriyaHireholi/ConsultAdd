def count_customers(computers, people):
    occupied = 0
    seen = {}
    walked_away = 0
    for p in people:
        if p not in seen:
            seen[p] = True
            if occupied < computers:
                occupied += 1
            else:
                seen[p] = False
                walked_away += 1
        else:
            occupied -= 1
    return walked_away

def main():
    user_input1 = int(input("Enter number of computers: "))
    user_input2 = input("Enter string: ")
    ans = count_customers(user_input1, user_input2)
    print(f"Output: {ans}")

if __name__ == "__main__":
    main()
