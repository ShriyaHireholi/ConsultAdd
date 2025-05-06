def JtoI(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        corrected = content.replace('J', 'I')
        return corrected
    except FileNotFoundError as e:
        return(f"Error: The file not found.")

def main():
    f = input("Enter file path: ")
    ans = JtoI(f)
    print(f"Result:\n{ans}")

if __name__ == "__main__":
    main()
