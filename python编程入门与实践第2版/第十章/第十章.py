

# with open("test.txt", "r") as file_object:
#     file_stream = file_object.readlines()
#     # print(file_stream)
# pi_string = ''
# for i in file_stream:
#     pi_string += i
# print(pi_string)
# print(len(pi_string))
# print(pi_string.splitlines(True))
    # print(i.splitlines(True))


# def print_long_line():
#     print("The door bursts open. A MAN and WOMAN enter, drunk and giggling,"
#           "horny as hell.No sooner is the door shut than they're all over each other,"
#           "ripping at clothes,pawing at flesh, mouths locked together.")
#
# print_long_line()


# practice 10-3
# while True:
#     user = input('Pleash input your name: ')
#     if user == 'q':
#         break
#     with open("guests.txt", 'a', encoding='utf-8') as p:
#         p.write(user + '\n')


# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError as e:
#         print(e)
#         print("You can't divide by 0!")
#     else:
#         print(answer)
#
# import json
# a = [1, 2, 3, 4, 5]
# b = str(a)
# print(a)
# for i in range(5):
#     with open('text.json', 'a') as p:
#         number = json.dump(a, p)
#
# with open('text.json', 'r') as q:
#     num = json.load(q)
#     print(num)
# print(isinstance(num, list))  # True
# with open('text.json', 'w') as w:
#     w.write(b)


import json
def greet_user():
    """问候用户，并指出其名字。"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")
greet_user()