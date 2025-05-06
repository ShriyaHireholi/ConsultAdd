class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, t):
        total_minutes = self.minutes + t.minutes
        extra_hours = total_minutes // 60
        total_minutes %= 60
        total_hours = self.hours + t.hours + extra_hours
        return total_hours, total_minutes

    def displayTime(self):
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinute(self):
        print(f"{self.hours * 60 + self.minutes} minutes")

def main():
    print("Enter hours and minutes to create 2 time objects")
    hr1 = int(input("Enter hour for 1st object: "))
    min1 = int(input("Enter min for 1st object: "))
    hr2 = int(input("Enter hour for 2nd object: "))
    min2 = int(input("Enter min for 2nd object: "))

    t1 = Time(hr1, min1)
    t2 = Time(hr2, min2)
    hr, min = t1.addTime(t2)
    print(f"Total hours and minutes: {hr} hours & {min} minutes")
    t1.displayTime()
    t1.displayMinute()

if __name__ == "__main__":
    main()
