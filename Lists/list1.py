colors1 = ["blue", "red", "orange"]
colors2 = ["violet", "purple", "blue"]
colors3 = ["lime", "green", "black"]


print(colors1)

# Part 2: append to empty list.
colors2 = []
colors2.append("blue")
colors2.append("red")
colors2.append("orange")
print(colors2)

# Part 3: use list built-in with existing list.
colors3 = list(colors2)
print(colors3)
