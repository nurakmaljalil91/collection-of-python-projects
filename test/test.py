# def initial(phrase):
#     words = phrase.split()
#     result = ''
#     for word in words:
#         for w in word:
#             if w.isupper():
#                 result += ''.join(w)
#     return result

# print(initial('this is my life'))


# def group_list(group, users):
#     members = ','.join(users)
#     return '{}:  {}'.format(group, members)

# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"

# def guest_list(guests):
#     for n in guests:
# 	    g = n
# 	    print('{} is {} years old and works as {}'.format(g[0],g[1],g[2]))

# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)

# print(wardrobe)
# animal = "Hippopotamus"
# print(animal[3:6])
# print(animal[-5])
# print(animal[10:])

# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)


# host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
# print(host_addresses.keys())

help("")