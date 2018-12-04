import re

claims = []
with open('../input.txt') as file:
    for line in file:
        result = re.search(r"(.*) @ (\d+),(\d+): (\d+)x(\d+)", line)
        if result:
            claims.append([int(result.group(2)), int(result.group(3)), int(result.group(4)), int(result.group(5))])

limits = ([[line[0] + line[2], line[1] + line[3]] for line in claims])
width = max(limits, key=lambda x: x[0])[0] + 1
height = max(limits, key=lambda x: x[1])[1] + 1
print(width, height)

area = [[0] * width for i in range(height)]

for line in claims:
    for x in range(line[2]):
        for y in range(line[3]):
            area[line[0] + x][line[1] + y] += 1

result = sum(map(sum, ([[int(val >= 2) for val in line] for line in area])))
print(result)
