# Input list.
elements = [0, 10, 20, 30]

# Use range.
for i in range(1, len(elements)):
    # Get two adjacent elements.
    a = elements[i - 1]
    b = elements[i]

    # Print 2 elements.
    print(a, b)
