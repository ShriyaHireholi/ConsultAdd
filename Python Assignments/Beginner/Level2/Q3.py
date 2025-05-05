def subseq_count(l1, k):
    count = 0
    seen = set()

    for num in l1:
        complement = k - num
        if complement in seen:
            count += 1
        seen.add(num)

    return count

def main():
    user_input1 = input("Enter array length: ")
    num_list1 = [i for i in range(1, int(user_input1) + 1)]
    k = int(input("Enter an integer k: "))
    ans = subseq_count(num_list1, k)
    print(f"Number of pairs: {ans}")

if __name__ == "__main__":
    main()
