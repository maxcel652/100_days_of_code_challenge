name1 = input("what is your name? ").lower()
name2 = input("what is his name? ").lower()
combined_name = name1 + name2

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true_total = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love_total = l + o + v + e 

true_love = int(str(true_total) + str(love_total))

print(true_love)
