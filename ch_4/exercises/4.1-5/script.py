# kadane's algorithm for maximum sum sub array in linear time
from typing import List, Tuple


def max_sub(data: List[int]) -> Tuple[List[int], int, int]:
    """calculates the maximal subarray

    Returns:
        Tuple[List[int], int, int, int]: a maximal subarray, lower index, upper index, sum
    """

    if len(data) == 1:
        return data, 0, 0

    # finding the array too requires linear space
    # finding max sum would require constant space

    end_sums = [data[0]]
    max_sum = data[0]
    max_end_index = 0

    for i in range(1, len(data)):
        check = end_sums[i-1] + data[i]

        if check > data[i]:
            end_sums.append(check)
        else:
            end_sums.append(data[i])

        if(end_sums[i] > max_sum):
            max_sum = end_sums[i]
            max_end_index = i

    # finding the lower index
    temp_sum = 0
    max_start_index = None
    for i in range(max_end_index, -1, -1):
        temp_sum += data[i]
        if temp_sum == max_sum:
            max_start_index = i

    return data[max_start_index: max_end_index+1], max_start_index, max_end_index, max_sum


data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_sub(data)

print('input', data)
print('a maximal sub array', result[0])
print('lower index', result[1])
print('upper index', result[2])
print('sum value', result[3])
