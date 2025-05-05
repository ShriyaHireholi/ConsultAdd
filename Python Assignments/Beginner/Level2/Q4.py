def rotate_arr(l1, d):
    l1 = l1[d::-1] + l1[:d:-1]
    return l1[::-1]

def main():
    user_input1 = input("Enter numbers separated by space for 1st list: ")
    num_list1 = [int(x) for x in user_input1.split()]
    d = int(input("Enter a integer d to rotate: ")) % len(num_list1)
    ans = rotate_arr(num_list1, d)
    print(f"Array after Rotation: {ans}")

if __name__ == "__main__":
    main()
