print ("==================================")
print ("Welcome here")
print ("my first post!")
print ("==================================")

username = "cool_creator"
bio = "Fun Blogger"
followers = 100     

print ("Username: ", username)
print ("Bio: ", bio)
print ("Followers: ", followers)

followers += 50
print ("Day 1: ", followers)

followers += 20
print ("Day 2: ", followers)

followers += 10
print ("Day 3: ", followers)


username = input("Enter Username: ")
age = input("Enter Age: ")
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("===================")
print("Username: ", username)
print("Age: ", age)
print("Content Category: ", category)

if int(age) > 40 and category == "fun":
    print("You are too old what is fun for you??")