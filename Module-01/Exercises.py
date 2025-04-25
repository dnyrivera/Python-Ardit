"""
(1) prompts the user to input their name once, and
(2) repeatedly prints out the name with the first letter capitalized.
"""

# user_name = input("Enter your name:").strip().title()
# while True:
#     print(f"{user_name}")

"""
(1) prompts the user to input their name,
(2) prints out the name with the first letter capitalized,
(3) keeps prompting the user to input another name
(4)  prints out the name with the first letter capitalized,
(5) The process is repeated infinitely.
"""
# while True:
#     user_name = input("What is your name?: ").strip().capitalize()
#     print(user_name)

"""
(1) prints out the methods of the list type, and
(2) prints out the help of the list.count method
"""
print(dir(list))
print(help(list.count))
