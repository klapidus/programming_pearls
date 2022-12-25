from datetime import datetime

import numpy as np


def split(ar):
    m = ar[0]
    l, r = [], []
    for x in ar[1:]:
        if x <= m:
            l.append(x)
        else:
            r.append(x)
    return l, m, r

def qsort(ar):
    if len(ar) < 2:
        return ar
    l, m, r = split(ar)
    return qsort(l) + [m] + qsort(r)


if __name__ == "__main__":
    size = 1_000_000
    array = np.random.randint(10000, size=size).tolist()
    #array = list(range(size))
    start = datetime.now()
    qsort(array)
    print('qsort time', (datetime.now()-start).total_seconds())

    start = datetime.now()
    sorted(array)
    print('timsort time', (datetime.now() - start).total_seconds())

    start = datetime.now()
    np.sort(array)
    print('npsort time', (datetime.now() - start).total_seconds())


    for _ in range(1000):
        size = np.random.randint(10)
        array = np.random.randint(10000, size=size)
        random_offset = np.random.randint(500)
        array = array - random_offset
        assert np.array_equal(np.sort(array), qsort(array))
