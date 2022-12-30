# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name(s):         Saylor Sherrodd
#                   Ricardo Mejia
#                   Spencer Jones
#                   Anderson Loan
#                   Andrew Spears
# Section:         574
# Assignment:   Lab 5.3
# Date:         20 9 2022
#

from math import e
#takes in all user inputs as a simple response
sex = input("Enter your sex (M/F): \n")
age = int(input("Enter your age(years): \n"))
bmi = float(input("Enter your BMI: \n"))
hypertensiveMed = input("Are you on medication for hypertension (Y/N)? \n")
steroidMed = input("Are you on steroids (Y/N)? \n")
smoking = input("Do you smoke cigarettes (Y/N)?")


#sets up all previous variables to upper if string for when we check them in our if statements
smoking = smoking.upper()

hypertensiveMed = hypertensiveMed.upper()
steroidMed = steroidMed.upper()
sex = sex.upper() 

#solves for smoking value 
if smoking == "N":
    smoking = input("Did you used to smoke (Y/N)?")
    smoking = smoking.upper()
    if smoking == "N":
        smoking = 0
    else:
        smoking = -0.218 
else:
    smoking = 0.855 
history = input("Do you have a family history of diabetes (Y/N)?")
history = history.upper()
#solves for the history value
if history == "Y":
    #sees if the idnvidual history is with both parents
    history = input("Both parent and sibling (Y/N)?")
    history = history.upper()
    if history == "Y":
        history = 0.753 
    else:
        history = 0.728
else:
     history = 0
#solves for the sex value
if sex == "M":
    sex = 0 
else:
    sex = 0.879
    
#solves for the BMI value
if bmi < 25: 
    bmi = 0
elif bmi >= 25 and bmi <= 27.49:
    bmi = 0.699
elif bmi >= 27.5 and bmi <= 29.99:
    bmi = 1.97
elif bmi >= 30:
    bmi = 2.518

#slves for steroid value
if steroidMed == "Y":
    steroidMed = 2.191
else:
    steroidMed = 0

#solve for hypertensiveMed value
if hypertensiveMed == "Y":
    hypertensiveMed = 1.222
else:
    hypertensiveMed = 0

#solves for % change of type 2 
n = 6.322 + sex - (0.063 * age) - bmi - hypertensiveMed - steroidMed - smoking - history
risk = 100/(1+(e**n))
print(f"Your risk of developing type-2 diabetes is {risk:.1f}%")

