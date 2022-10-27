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
