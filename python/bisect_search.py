import numpy as np


def bisect_search(array, x):
    size = len(array)
    if size == 0:
        return False
    elif size == 1:
        if array[0] == x:
            return True
        else:
            return False
    else:
        mid_element = array[size//2]
        if mid_element == x:
            return True
        elif mid_element > x:
            return bisect_search(array[:size//2], x)
        else:
            return bisect_search(array[size//2 + 1:], x)


for _ in range(10000):
    size = np.random.randint(1000)
    array = np.random.randint(10000, size=size)
    random_offset = np.random.randint(500)
    array = array - random_offset
    array_sorted = np.sort(array).tolist()
    x = np.random.randint(1000) - np.random.randint(500)
    assert bisect_search(array_sorted, x) == (array[array==x].size > 0)
