# rotate an array using the reverse trick
# as described in Programming Pearls

def reverse(ar):
    return ar[::-1]


def rotate(ar, k):
    n = len(ar)
    if k > n:
        k = k % n
    l, r = ar[:k], ar[k:]
    return reverse(reverse(l) + reverse(r))


if __name__ == "__main__":
    tar = [1, 2, 3, 4, 5, 6]
    print(tar)
    print(rotate(tar, 0))
    print(rotate(tar, 3))
    print(rotate(tar, 9))
    print(rotate(tar, 10))
    print(rotate(tar, 12+3))
