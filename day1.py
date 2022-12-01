elfes = []

# Read inputs
with open("input.txt", "r") as inputFile:
    elf = 0
    for line in map(lambda l: l.strip(), inputFile.readlines()):
        if len(line) > 0:
            elf += int(line)
        else:
            elfes.append(elf)
            elf = 0
    elfes.append(elf)

# Sort elfes by amount of carried calories (reverse because descending)
elfes.sort(reverse=True)

# Compare carried calories and get the total calories of the top 3
print(f"Most carried calories by 1 elf: {elfes[0]}")
print(f"Top 3 total: {sum(elfes[:3])}")