def stone_piles(n):
    stones = []
    curr = 1 if n % 2 == 1 else 2
    total = 0
    while total + curr <= n:
        stones.append(curr)
        total += curr
        curr += 2
    return stones

def main():
    n = int(input("Enter number of stones: "))
    ans = stone_piles(n)
    print(f"Stone Piles: {ans}")

if __name__ == "__main__":
    main()
