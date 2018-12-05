import re

shifts = {}
with open('../input.txt') as file:
    content = file.readlines()
    content.sort()
    for line in content:
        result = re.search(r"\[(.*) (.*)\] (.*)", line)
        if result:
            date, time, event = result.group(1), result.group(2), result.group(3)
            minutes, seconds = time.split(':')
            if event.startswith('Guard'):
                _, guard, _ = event.split(' ', 2)
                if guard not in shifts:
                    shifts[guard] = {}
            elif event == 'falls asleep':
                if date not in shifts[guard]:
                    shifts[guard][date] = [0] * 60
                shifts[guard][date] = [shifts[guard][date][i] if i < int(seconds) else 1 for i in range(60)]
            elif event == 'wakes up':
                shifts[guard][date] = [shifts[guard][date][i] if i < int(seconds) else 0 for i in range(60)]

asleep_guard = None
max_minutes_asleep = 0
for guard, shift_item in shifts.items():
    total = [0] * 60
    # sum guard minutes all together
    for _, shift in shift_item.items():
        total = [total[i] + shift[i] for i in range(len(total))]
    shifts[guard]['total'] = total
    if asleep_guard is None:
        asleep_guard = guard
    elif sum(total) > sum(shifts[asleep_guard]['total']):
        asleep_guard = guard

max_minutes = max(shifts[asleep_guard]['total'])
max_index = shifts[asleep_guard]['total'].index(max_minutes)
print(int(asleep_guard[1:]) * max_index)


