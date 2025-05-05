def analyze_temp(l1):
    avg = sum(l1)/len(l1)
    return avg, max(l1), min(l1)

def main():
    user_input1 = input("Enter temperature separated by space: ")
    num_list1 = [int(x) for x in user_input1.split()]
    av, mx, mn = analyze_temp(num_list1)
    print(f"\nAverage Temp: {av:.1f} \nHighest Temperature: {mx} \nLowest Temperature: {mn}")

if __name__ == "__main__":
    main()
