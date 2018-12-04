freq_list = []
with open('../input.txt') as file:
    for line in file:
        freq_list.append(int(line))

acc = 0 + sum(freq_list)
print(acc)
