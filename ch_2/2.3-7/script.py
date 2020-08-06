from typing import List
from random import randint


def find_pair(data: List[int], target: int) -> (int, int):
    data.sort()

    # find element less than target

    start_index = 0
    for i in range(len(data)):
        if data[i] > target:
            break
        start_index = i

    ptr_2 = start_index
    ptr_1 = 0

    move_2 = False
    move_1 = True

    found = False

    while(ptr_2 > ptr_1):

        required_value = target - data[ptr_2]
        v1 = data[ptr_1]

        if v1 == required_value:
            found = True
            break

        if v1 > required_value:
            move_1 = False
            move_2 = True

        if v1 < required_value:
            move_1 = True
            move_2 = False

        if(move_1):
            ptr_1 += 1

        if(move_2):
            ptr_2 -= 1

    # if found:
    #     print(
    #         f'FOUND! ... lower {data[ptr_1]}, higher {data[ptr_2]}, {data[ptr_1]} + {data[ptr_2]} = {data[ptr_1] + data[ptr_2]}')

    # else:
    #     print('not found')

    return found


passed = True
trials = 0
for i in range(10**6):
    d = []
    for j in range(100):
        d.append(randint(0, 500))

    index_1 = randint(0, 99)
    value_1 = d[index_1]

    index_2 = randint(0, 99)
    value_2 = d[index_2]

    while(index_2 == index_1):
        index_2 = randint(0, 99)
        value_2 = d[index_2]

    result = find_pair(d, value_1 + value_2)

    trials += 1

    if not result:
        passed = False
        print('Failed at', i)
        d.sort()
        print('i1, v1', index_1, value_1)
        print('i2, v2', index_2, value_2)

        print(d)
        break

if(passed):
    print('____________SUCCESS_________________', 'trials =', trials)
else:
    print('____________FAILED_________________')
