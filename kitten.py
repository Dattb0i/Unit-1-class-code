'''
August Doe
10/9/24
Determine a cat's cost based on it's age using if statements and input.
'''



#Approach 1
age = int(input("How old is the cat in months?"))

if age <= 6:
    print(f"The kitten costs $250")

elif age >=7 and age <=11:
    print(f"The teenager costs $225")

elif age >=12 and age <= 95:
    print(f"The adult cat costs $150")

elif age >= 96:
    print(f"The senior cat costs $85")


#Approach 2
age2 = int(input("How old is the cat in months?"))

if age2 >= 96:
    print(f"The senior cat costs $85")

elif age2 >=12 and age2 <=95:
    print(f"The adult cat costs $150")

elif age2 >=7 and age2 <=11:
    print(f"The teenager costs $225")

elif age2 <= 6:
    print(f"The kitten costs $250")



#Approach 3
age3 = int(input("How old is the cat in months?"))

if age3 <= 6:
    print(f"The kitten costs $250")

if age3 >=7 and age3 <=11:
    print(f"The teenager costs $225")

if age3 >=12 and age3 <=95:
    print(f"The adult cat costs $150")

if age3 >= 96:
    print(f"The senior cat costs $85")



#Approach 4
age4 = int(input("How old is the cat in months?"))

if age4 >= 96:
    print(f"The senior cat costs $85")

if age4 >=12 and age4 <=95:
    print(f"The adult cat costs $150")

if age4 >=7 and age4 <=11:
    print(f"The teenager costs $225")

if age4 <= 6:
    print(f"The kitten costs $250")