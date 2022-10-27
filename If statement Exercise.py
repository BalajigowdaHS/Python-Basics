## 1) Using following list of cities per country,
#india = ["mumbai", "banglore", "chennai", "delhi"]
#pakistan = ["lahore","karachi","islamabad"]
#bangladesh = ["dhaka", "khulna", "rangpur"]
## 1.1) Write a program that asks user to enter a city name and it should tell which country the city belongs to


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter the city name :")

if city in india:
    print(f"The {city} is in india")

elif city in pakistan:
    print(f"The {city} is in Pakistan")

elif city in bangladesh:
    print(f"The {city} is in Bangladesh")
else :
    print("The country is not Mentioned in the list")
    
    ## 1.2) Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
# For example if I enter mumbai and chennai, it will print "Both cities are in India"
# but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter the city name")
city2 = input("Enter the city name")

if city1 in india and city2 in india:
    print("Both cities are in india")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in bangladesh")
else:
    print("They don't belong to same country")
