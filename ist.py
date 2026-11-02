# # # # def get_welcome_message():

# # # # 	return 'welcome to python'

# # # # message = get_welcome_message()

# # # # print(message)


# # # def double_number(num):
# # # 	return num *2

# # # print(double_number(5))
# # # print(double_number(12))

# # # def greet_user(name, greeting="hello"):
# # # 	return f"{greeting}, {name}"

# # # print(greet_user("Alex"))
# # # print (greet_user("sarah", "welcome"))

# # def can_vote(age):
# # 	return age >=18

# # print(can_vote(19))




def sum_all(*numbers):
	return f"sum is ={sum (numbers)}"

print(sum_all(1,3,4,5))

# def build_profile(first_name, last_name, **info):
#     # Notice we return a dictionary {} instead of an f-string f""
#     return f{"first_name": first_name,
#      "last_name": last_name,
#       **info}


# user = build_profile("corey", "something", age=18, location="sopore")
# print(user)
# # Output: {'first_name': 'corey', 'last_name': 'something', 'age': 18, 'location': 'sopore'}





# def hello():
# 	return'Hello, World!'
# 	print(hello())