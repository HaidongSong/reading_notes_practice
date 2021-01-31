print(type(range(10)), range(10))

squares = []
for value in range(1, 11, 2):
    squares.append(value ** 2)
print(squares)

for i in range(1, 21):
    print(i)

one_milion = [j for j in range(1, 1_000_000)]
print(one_milion)
# for k in one_milion:
#     print(k)
print(min(one_milion))
print(max(one_milion))
print(sum(one_milion))

odd_numbers = [m for m in range(3, 31) if m % 3 == 0]
print(odd_numbers)

lifang = [n**3 for n in range(1, 11)]
print(lifang)

# practice 4-10
myfoods = ["土豆泥", "土豆饼", "土豆条", ["土豆丝", "土豆棒"]]
favorite = myfoods[:]  # 浅拷贝

myfoods.append("土豆块")
print(myfoods)
print(favorite)
favorite[3].append("土豆皮")
print(myfoods)
print(favorite)

# practice 4-6
foods = ("cake", "cake", "sandwich", "steak", "pizza")
foods = (1, 1, 2, 2, 3, 4, 5)
for m in foods:
    print(m)
print(foods)
print(foods[1])
# foods[1] = "steak"
print(foods)
foods = ("snadwich", "pizza")
print(foods)

mylist = [1, 2, 1, 2, 1]  # 元祖定义的时候可以有重复元素，set()方法返回的元祖没有重复元素
print(mylist)
print(set(mylist))


for n in range(10):
    print(n)
