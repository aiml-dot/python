print("-----------SCHOLORSHIP ELIGIBLITY CHEAKER----------")

name = input("Enetr Your Name : ")
age = int(input("Enter your age : "))
income = float(input("Enter your annual family income ($) : "))
caste = input("Enter your caste(OBC / SC / ST ) : ")

if age < 25 and income < 300000:
    print(" \nCONGRATULATIONS!")
    print(name, " You Are Eligible For Scholorship ")
else:
        print(name," You Are Not Eligible For Scholorship ")  
