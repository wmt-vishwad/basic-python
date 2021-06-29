lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["abc", "pqr", "xyz", "mno", "stv"]
friends.extend(lucky_numbers)
print(friends)

friends.append("cre")
print(friends)

friends.insert(1,"kel")
print(friends)

friends.remove("cre")
print(friends)

friends.clear()
print(friends)

friends = ["abc", "pqr", "xyz", "mno", "stv"]
friends.pop()
print(friends)

print(friends.index("xyz"))

print(friends.count("abc"))

friends.sort()
print(friends)

friends2 = friends.copy()
print(friends2)
