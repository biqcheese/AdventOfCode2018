def react(polymer):
    diff = abs(ord('a') - ord('A'))
    reacted = False
    for i in range(0, len(polymer) - 1):
        if abs(ord(polymer[i]) - ord(polymer[i+1])) == diff:
            polymer = polymer[:i] + polymer[i+2:]
            reacted = True
            break
    return polymer, reacted


with open('../input.txt') as file:
    chain = file.readline()


boom = True
while boom:
    chain, boom = react(chain)
    print(len(chain))
