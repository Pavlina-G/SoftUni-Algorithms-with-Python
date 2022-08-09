import itertools

names = input().split(', ')
people = [None] * len(names)

while True:
    command = input()
    if command == 'generate':
        break
    name, sit = command.split(' - ')
    place = int(sit)
    index = place - 1

    people[index] = name
    names.remove(name)

result = list(itertools.permutations(names))

for perm in result:
    index = 0
    output = []
    for i in range(len(people)):
        if people[i] is not None:
            output.append(people[i])
        else:
            output.append(perm[index])
            index += 1
    print(' '.join(output))
