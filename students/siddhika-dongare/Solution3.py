def classify_grade(s):
    if s >= 90:
        print("A")
    elif s > 80 and s <= 90:
        print("B")
    elif s >= 70 and s <=80:
        print("C")
    elif s >= 60 and s <=70:
        print("D")
    else:
        print("F")

# function call
score = int(input("enter your score:"))
classify_grade(score)

#problem2
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(True)
    else:
        print(False)

year= int(input("enter a year:"))
is_leap_year(year)

#problem3

