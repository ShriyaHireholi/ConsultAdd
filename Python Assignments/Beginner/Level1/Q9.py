def count_freq(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

def main():
    user_input = input("Enter numbers separated by space: ")
    num_list = [int(x) for x in user_input.split()]
    ans = count_freq(num_list)
    print(f"Frequency Count: {ans}")

if __name__ == "__main__":
    main()
