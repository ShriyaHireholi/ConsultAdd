def count_lines(filename):
    try:
        with open(filename, 'r') as f:
            return len(f.readlines())
    except FileNotFoundError as e:
        return(f"Error: The file not found.")

def main():
    f = input("Enter file path: ")
    ans = count_lines(f)
    print(f"Total Number of Lines in the file: {ans}")

if __name__ == "__main__":
    main()
