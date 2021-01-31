# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")
#
# # practice 7.2
#
# nums = input("Please input people numbers:")
# if int(nums) > 8:
#     print("Sorry, there are no free tables.")
# else:
#     print("47 is free tables. Please wait!")

# num = input("Please input a number")
# if int(num) % 10 == 0:
#     print("This number is 10 的倍数")
# else:
#     print("这个数字不是10的倍数")


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# sandwiches_orders = ["yellow", "green", "blue", "yellow", "yellow"]
# finish_sandwiches = []
# print("yellow is sales")
# while "yellow" in sandwiches_orders:
#     sandwiches_orders.remove("yellow")
# print(sandwiches_orders)
# while sandwiches_orders:
#     i = sandwiches_orders.pop()
#     print(f"I made your {i} sandwich.")
#     # sandwiches_orders.remove(i)
#     finish_sandwiches.append(i)
# print(sandwiches_orders, finish_sandwiches)

# def describe_pet(animal_type, pet_name):
# # """
# # 显示宠物的信息。
# # """
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet(animal_type='hamster', pet_name='harry')

# practice 第八章 8-9

def show_message(info, new_info):
    print(info)
    print(new_info)
    while info:
        info_pop = info.pop()
        new_info.append(info_pop)


messages = ["hello,", "bob dylan", "how are you"]
show_message_list = []
show_message(messages[:], show_message_list)

print(f"messages:{messages}, show_message:{show_message_list}")

print(show_message)
# def print_models(unprinted_designs, completed_models):
#     """
#     模拟打印每个设计，直到没有未打印的设计为止。
#     打印每个设计后，都将其移到列表completed_models中。
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """
#     显示打印好的所有模型。
#     """
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

print(__name__)