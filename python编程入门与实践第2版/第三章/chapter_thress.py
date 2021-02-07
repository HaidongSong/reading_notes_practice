names = ["bob", "dylan", "margan", "eric"]

for i in names:
    print(f"Hello, {i.title()}")

traffic = ['bike', "car", "bus", "subway"]

print(f"I would like to own Honda {traffic[0]}")

# practice 3-6
for j in names:
    print(f"I like to invite {j.title()} to dinner.")

names.insert(0, "lisa")
print(names)
names.insert(2, "lady")
print(names)
names.append("ppx")
print(names)

print("Sorry, I invite two friends to dinner.")
names.pop(0)
names.pop(1)
names.pop()
names.pop()
names.pop()
print(names)
for k in names:
    print(f"My friends, You are still invited:{k.title()}")

# del names[0]
# del names[1]
print(names)


# practice 3-9

city = ["california", "kunming", "haerbing", "maerdaifu"]
print(city)
print(sorted(city))
print(city)
city.reverse()
print(city)

print(city.sort())
print(city)
city.sort(reverse=True)
print(city)
print(type(reversed(city)), reversed(city))
city_reversed = reversed(city)
for m in city_reversed:
    print(m)
print(city)

