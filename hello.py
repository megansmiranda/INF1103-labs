username = input("Enter your username: ")
age = int(input("Enter your age: "))
category = input("Enter Category: ")

print("\nInstagram Profile")
print("===============================")
print("Username:", username)
print ("Age:", int(age))
print("Category:", category)

if age>40 and category=="fun":
    print("You are too old, what is fun for you??")
