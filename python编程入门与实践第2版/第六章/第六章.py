cat = {"name": "kiki", "master_name": "bob"}
dog = {"name": "tom", "master_name": "dylan"}

pets = [cat, dog]
for i in pets:
    print(f"{i['name']}'s master is {i['master_name']}")

favorite_place = {
    "bob": ["广州", "太远", "憋精"],
    "dylan": ["北京", "上海", "天津"]
}

for k, v in favorite_place.items():
    print(f"{k} favorite city is {', '.join(v)}.")