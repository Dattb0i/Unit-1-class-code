'''
Name: August Doe
Date: 9/30/24
Description: Unit 2 Homework 1
'''

print('Problem 1'.center(20,'-'))

print("One idea I have is to ask the user what path to choose out of the options.")

print("Another idea is to have them fight some sort of monster.")

print("My final idea is to have them do a puzzle where if they get it wrong they have to restart the entire thing.")

print('Problem 2'.center(20,'-'))
goblin = r'''        
        .-"""".
       /       \
   __ /   .-.  .\
  /  `\  /   \/  \
  |  _ \/   .==.==.
  | (   \  /____\__\
   \ \      (_()(_()
    \ \            '---._
     \                   \_
  /\ |`       (__)________/
 /  \|     /\___/
|    \     \||VV
|     \     \|"""",
|      \     ______)
\       \  /`
         \(
'''
print(goblin)

print('Problem 3'.center(20,'-'))
distance = 173.8
mpg = int(input("How many miles per gallon does your car get?"))
cost = float(input("How much does a gallon of gas cost near you?"))
tank_capacity = int(input("How much gas can your car hold?"))
#(cost*tank_capacity) #cost to fill up your tank
#(distance/mpg)(cost) #cost to do the trip
print(f"Your trip will cost ${distance/mpg: .2f}")
print(f"If you fill up your tank, your trip will cost ${cost*tank_capacity: .2f}")

