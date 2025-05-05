import math
def find_lcm(n, m):
    lcm = abs(n*m) // math.gcd(n,m)
    return lcm

def main():
    print("Enter a numbers to find their LCM ")
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    ans = find_lcm(num1, num2)
    print(f"LCM of {num1} and {num2} are: {ans}")

if __name__ == "__main__":
    main()