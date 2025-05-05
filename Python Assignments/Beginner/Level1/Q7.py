import re
def anagram_string(s1, s2):
    s1 = sorted(re.findall(r"[a-zA-Z]", s1.lower()))
    s2 = sorted(re.findall(r"[a-zA-Z]", s2.lower()))
    if s1 == s2:
        return True
    return False
    

def main():
    print("Input two strings to check if they are anagram")
    str1 = input("String1: ")
    str2 = input("String2: ")
    print(anagram_string(str1, str2))

if __name__ == "__main__":
    main()