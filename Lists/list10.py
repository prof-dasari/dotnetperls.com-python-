# Unsorted list.
values = ["bbb", "aaa", "ccc"]

# Version 1: call sort.
values.sort()
print(values)

# Another unsorted list.
values2 = ["bbb", "aaa", "ccc"]

# Version 2: use sorted view on a list.
for value in sorted(values2):
    print(value)
