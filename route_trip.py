import progressbar
import time
print("TripMe Backend")

user_current_location = "Delhi, India"
print("Current Location \n"+user_current_location)

print("Enter Food Preferences : ")
print("1 . Veg")
print("2 . Non Veg")
user_food_preference = int(input())

if user_food_preference == 1:
    print("Veg is your food preference")
elif user_food_preference == 2:
    print("Non Veg is your food preference")
else:
    print("You have no food preference")

user_budget = int(input("Enter Budget for your trip "))
print("Your Budget : "+str(user_budget))

user_duration_of_trip = int(input("Enter duration of your trip"))
print("Your duration of trip : "+str(user_duration_of_trip))

print("Planning the best possible route")

for i in progressbar.progressbar(range(100)):
    time.sleep(0.02)

print("Route and Checkpoint Plan")
print("Book a Cab to the nearest Hotel (Best Price)")
