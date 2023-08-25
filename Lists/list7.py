list = []
f = open("example.txt", "r")

# Loop through all lines.
for line in f.readlines():
    # Strip each line to remove trailing newline.
    list.append(line.strip())

print(list)
