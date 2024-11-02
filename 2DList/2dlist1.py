# Step 1: create a list.
# ... Append empty lists in first two indexes.
elements = []
elements.append([])
elements.append([])

# Step 2: add elements to empty lists.
elements[0].append(1)
elements[0].append(2)

elements[1].append(3)
elements[1].append(4)

# Step 3: display top-left element.
# ... Display entire list.
print(elements[0][0])
print(elements)

# Step 4: loop over rows.
for row in elements:
    # Loop over columns.
    for column in row:
        print(column, end="")
    print(end="\n")
