with open('../input.txt') as file:
    letters_list = file.readlines()

occurences = [[line.count(chr(letter)) for letter in range(ord('a'), ord('z') + 1)] for line in letters_list]
result = sum([2 in line for line in occurences]) * sum([3 in line for line in occurences])
print(result)
