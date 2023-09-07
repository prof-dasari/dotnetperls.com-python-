ids = [201, 202, 203]

# Loop over the list indexes in reverse order (from last to first).
# ... We go from the length and stop after 1.
#     So we must subtract 1 to get the indexes.
for i in range(len(ids), 0, -1):
    print("INDEX:", i - 1)
    print("ID:", ids[i - 1])
