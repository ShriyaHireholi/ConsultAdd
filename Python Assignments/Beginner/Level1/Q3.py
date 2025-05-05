def calculate_percentage(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"

def main():
    print("Enter marks out of 100 for each subject:")
    physics = float(input("Physics: "))
    chemistry = float(input("Chemistry: "))
    biology = float(input("Biology: "))
    math = float(input("Mathematics: "))
    computer = float(input("Computer: "))

    total_marks = physics + chemistry + biology + math + computer
    percentage = (total_marks / 500) * 100
    grade = calculate_percentage(percentage)

    print(f"\nPercentage: {percentage:.2f}%  Grade: {grade}")

if __name__ == "__main__":
    main()