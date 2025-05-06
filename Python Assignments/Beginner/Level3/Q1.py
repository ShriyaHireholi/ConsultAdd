def even_len_words(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        ans = []
        for line in lines:
            words = line.split()
            for word in words:
                if len(word) % 2 == 0:
                    ans.append(word)
        return ' '.join(ans)
    except FileNotFoundError as e:
        return(f"Error: The file not found.")

def main():
    f = input("Enter file path: ")
    ans = even_len_words(f)
    print(f"Result: {ans}")

if __name__ == "__main__":
    main()
