#program 1 Check Employee promotion eligibility
age=int(input())
experience=int(input())
salary=int(input())
if(age>25 and experience>5 and salary>50000):
    print("eligible for promotion")
else:
    print("not eligible")
#program 2 Check student distinction category
math=int(input())
science=int(input())
english=int(input())
marks=math+science+english
if marks>=75:
    print("distinction")
elif marks>=35:
    print("pass")
else:
    print("fail")
#program 3 Check website login system
username = input("Enter username: ")
password = input("Enter password: ")
otp = input("Enter OTP: ")
if username == "admin" and password == "1234" and otp == "5678":
    print("Login Successful")
else:
    print("Invalid Credentials")
# program 4 Check internet package category
speed=int(input())
data=int(input())
rd=int(input())
if(speed>100 and data> 500 and rd>20):
    print("premium plan")
elif speed>50 and data>250 and rd>10:
    print("standard plan")
else:
    print("basic")
#program 5 Check job eligibility
degree=input()
experience=int(input())
age=int(input())
if(age>25 and experience>5 and degree=="yes"):
    print("eligible")
else:
    print("not eligible")
#program 6 Check flight boarding eligibility
ticket = input("Ticket available (yes/no): ")
passport = input("Passport available (yes/no): ")
luggage = int(input("Enter luggage weight: "))

if ticket == "yes" and passport == "yes" and luggage < 30:
    print("Boarding Allowed")
else:
    print("Boarding Denied")
#program 7 Check scholarship eligibility
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))
income = int(input("Enter family income: "))

if marks >= 85 and attendance >= 90 and income < 300000:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")
#program 8 Check mobile unlock system
pin = input("Enter PIN: ")
face = input("Face detection status (yes/no): ")
fingerprint = input("Fingerprint status (yes/no): ")

if pin == "1234" and face == "yes" and fingerprint == "yes":
    print("Mobile Unlocked")
else:
    print("Access Denied")
# program 9 Check hotel booking eligibility
rooms=int(input())
days=int(input())
budget=int(input())
if rooms>=2 and days>=3 and budget>=50000 :
   print("luxury booking")
elif(rooms>=1 and budget>10000):
    print("standard")
else:
    print("budget")
#program  10. Check exam topper category
sub1 = int(input("Enter Subject 1 marks: "))
sub2 = int(input("Enter Subject 2 marks: "))
sub3 = int(input("Enter Subject 3 marks: "))
total = sub1 + sub2 + sub3
if total >= 270:
    print("Topper")
elif total >= 180:
    print("Average")
else:
    print("Needs Improvement")
#program 11. Check gym membership category
age = int(input("Enter age: "))
weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

if age > 18 and weight > 50 and height > 5.5:
    print("Fitness Category A")
elif age > 18 and (weight > 50 or height > 5.5):
    print("Fitness Category B")
else:
    print("Basic Category")
#program 12 Check traffic penalty system
helmet=(input())
license=(input())
speed=int(input())
if(helmet=="yes" and license=="yes" and speed<80):
    print("no fine")
elif(speed>100):
    print("heavy fine")
else:
    print("normal fine")
#program 13 Check movie ticket pricing
age = int(input("Enter age: "))
day = input("Enter day: ")
member = input("Membership available (yes/no): ")

if age < 18 and member == "yes" and day == "Sunday":
    print("50% Discount")
elif member == "yes":
    print("25% Discount")
else:
    print("No Discount")
#program 14 Check weather alert system
temperature = float(input("Enter temperature: "))
wind = float(input("Enter wind speed: "))
rain = input("Rain status (yes/no): ")

if temperature > 40 and wind > 50 and rain == "no":
    print("Heat Alert")
elif wind > 50 and rain == "yes":
    print("Storm Alert")
else:
    print("Normal Weather")
#program 15 Check online shopping offer
amount=int(input())
coupon=(input())
member=(input())
if(member=="yes" and coupon=="yes" and amount>10000):
    print("amximum discount")
elif(amount>5000 and coupon=="yes"):
    print("medium discount")
else:
    print("no discount")
#program 16 Check server room access
idcard = input("ID card status (yes/no): ")
fingerprint = input("Fingerprint status (yes/no): ")
accesslevel = int(input("Enter access level: "))
if idcard == "yes" and fingerprint == "yes" and accesslevel > 5:
    print("Access Granted")
else:
    print("Access Restricted")
# program 17 Check sports team selection
speed = int(input("Enter speed score: "))
fitness = int(input("Enter fitness score: "))
discipline = int(input("Enter discipline score: "))
if speed > 80 and fitness> 80 and discipline > 80:
    print("Selected")
elif speed > 60 and fitness > 60 and discipline > 60:
    print("Waiting List")
else:
    print("Rejected")
#program 18 Check laptop purchase recommendation
budget = int(input("Enter budget: "))
ram = int(input("Enter RAM size: "))
storage = int(input("Enter storage size: "))
if budget > 100000 and ram >= 16 and storage >= 512:
    print("Gaming Laptop")
elif budget > 50000 and ram >= 8 and storage >= 256:
    print("Office Laptop")
else:
    print("Basic Laptop")
#program 19 Check bank loan approval
salary = int(input("Enter salary: "))
creditscore = int(input("Enter credit score: "))
experience = int(input("Enter experience in years: "))
if salary > 50000 and creditscore > 750 and experience > 3:
    print("Loan Approved")
elif salary > 30000 and creditscore > 650:
    print("Loan Under Review")
else:
    print("Loan Rejected")
#program 20 Check smart home security system
salary = int(input("Enter salary: "))
creditscore = int(input("Enter credit score: "))
experience = int(input("Enter experience in years: "))
if salary > 50000 and creditscore > 750 and experience > 3:
    print("Loan Approved")
elif salary > 30000 and creditscore > 650:
    print("Loan Under Review")
else:
    print("Loan Rejected")

