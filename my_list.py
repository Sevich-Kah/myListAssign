#list
my_list = []

#
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15
my_list.insert(1, 15)

# Extend my_list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# ascending order
my_list.sort()

# Find index of 30 in my_list
index_of_30 = my_list.index(30)

# Print the final list
print("Final List:", my_list)
print("Index of 30:", index_of_30)