print("**********COLLEGE ADMISSION ELIGIBILITY**********")

num_age = int(input("Enter your age :"))
num_mark = int(input("Enatr your mark :"))

if num_age>7 and num_age<25:
    print("you are eligible for addmision")

    if num_mark>60:
        if num_mark>80:
            print("you are eligible for AIML department")

        elif num_mark<80:
            print("you are eligile for CSE department")

    elif num_mark<70:
        print("you are eligible for general")


else:
    print("you are not eligile for addmision")
