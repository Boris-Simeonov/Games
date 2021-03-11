person1_name = input("What is the guys name?\n")
person2_name = input("What is the girls name?\n")
name = person1_name + person2_name
name = name.lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")

tens = t + r + u + e
singles = l + o + v + e
percent = tens*10 + singles

if percent<10 or percent>90:
	print(f"Your love score is {percent}%. You will have a boring Norwegian or exlossive Italian relationship.Run!")
elif 40 <= percent <= 50:
	print(f"Have no fear, you will be great. Your love score is the perfect {percent}%.")
else:
	print(f"You scored {percent}%. You can bang it out.")