name = input("Please type your name:")
age = int(input("Enter your age:"))
gpa = float(input("Enter your GPA (0-5):"))
foi = input("Field of interest:")
graduated=input("Are you graduated?(yes or no): ")

if (graduated == 'yes'):
    is_graduated = True
elif(graduated =='no'):
    is_graduated = False
else:
    print("Invalid input")
    

if (age<25 and gpa >=3.5 and is_graduated):
    print(f"{name} is eligible for a scholarship")
elif(age<30 and gpa>=2.5):
    print(f"{name} is eligible for an internship")
else:
    print("Please try again later")