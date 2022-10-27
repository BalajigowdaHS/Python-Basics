##1.Create 3 variables to store street, city and country, now create address variable to store entire address.
#Use two ways of ##creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line

Street = "10 street"
City = " Bengaluru"
Country = " India"
Address = Street +'\n'+ City + '\n'+  Country
print("The address is ", Address)

Street = "10 street"
City = " Bengaluru"
Country = " India"
print(f"The address is, {Street}, \n{City},\n{Country}" )

##2. Create a variable to store the string "Earth revolves around the sun"
##Print "revolves" using slice operator
##Print "sun" using negative index

Statement = 'Earth revolves around the sun'
print(Statement[6:14])
print(Statement[-3:])


##3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
# Use python f string for this.

number_of_vegei = "10"
number_of_fruits = "20"
print(f"I eat {number_of_vegei} veggies and {number_of_fruits} fruits")

##4. I have a string variable called s='maine 200 banana khaye'.
# This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

s = "maine 200 banana khaye"
s1 = s[0:5]+" 10 samosa" +s[14:]
print(s1)
