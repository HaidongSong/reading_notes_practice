# class Restaurant:
#     def __init__(self, restaurant_name, cuision_type):
#         self.restaurant_name = restaurant_name
#         self.cuision_type = cuision_type
#         self.served_number = 0
#
#     def describe_restaurant(self):
#         print(f"This is {self.restaurant_name}.")
#
#     def open_restaurant(self):
#         print(f"Open restaurant ,cuision type is {self.cuision_type}")
#
#     def set_served_number(self, num):
#         self.served_number = num
#         print(f"served_number: {self.served_number}")
#
#     def increment_served_number(self, inc_num):
#         self.served_number += inc_num
#         print("served_number:", self.served_number)

#
# restaurant = Restaurant("和平饭店", "油炸")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# print("------", restaurant.served_number)
# restaurant.set_served_number(200)
# print("--------", restaurant.served_number)
# restaurant.increment_served_number(100)
# print("--------", restaurant.served_number)

# practice 9-6


# class IceCreamStand(Restaurant):
#     def __init__(self):
#         super().__init__
#         self.flavors = ["ice", "fire", "yellow"]
#
#     def make_flavors(self):
#         for i in self.flavors:
#             print(i)
#
#
# ice = IceCreamStand()
# ice.make_flavors()


# mydict = {
#     "a": 1,
#     "b": {"aa": 2, "bb": 15},
#     "c": {"aa": 2, "bb": {"aaa": 222, "bbb":333}}
# }
#
#
# def trans_str(dic):
#     for k, v in dic.items():
#         if isinstance(v, dict):
#             trans_str(v)
#         else:
#             dic[k] = str(v)
#
#
# trans_str(mydict)
# print(mydict)


# def create_counter(n):
#     print("create_counter")
#     while True:
#         yield n
#         print("increment n")
#         n +=1
#
# gen = create_counter(2)
# print(gen)
# print(next(gen))
# print(next(gen))
# a = (s**2 for s in range(10))
# print(a)
# print(a.__iter__())
# for i in a:
#     print(i)

#
# class myYield():
#     def __init__(self, x):
#         self.a = x
#         self.b = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.b < self.a:
#             num = self.b
#             self.b += 1
#             return num
#         else:
#             raise StopIteration
#
#
# a = myYield(10)

# print(type(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#
#   def __next__(self):
#     if self.a <= 10:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration
#
#
# myclass = MyNumbers()
# myclass = iter(myclass)
#
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# # m = iter(myclass)
# # print(type(m))
# # for x in m:
# #   print(x)

# practice 9-5


import random


class Die:
    def __init__(self):
        self.sides = 6

    def roll_sides(self):
        print(random.randint(1, 6))

#
# a = Die()
# a.roll_sides()

# 9-14


def is_type(test):
    if isinstance(test, str):
        return str
    else:
        return int

n = 1


while True:
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 9, "a", "b", "c", "d", "f"]
    # print(random.choice(test_list))
    # print(type(1), type("111"))
    my_ticket = []
    for i in range(4):
        my_ticket.append(random.choice(test_list))
    print(my_ticket)
    if type(my_ticket[0]) == type(my_ticket[1]) ==type(my_ticket[2]) ==type(my_ticket[3]):
        print(f"Congratulation you, 第{n}次中奖")
        break
    n += 1


