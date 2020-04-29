swaps = 0


def countSwaps(li):
    for i in range(0, len(li)):
        for j in range(0, (len(li) - 1)):
            if li[j] > li[j + 1]:
                global swaps
                swaps += 1
                li[j], li[j + 1] = li[j + 1], li[j]
    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element:', li[0])
    print('Last Element:', li[-1])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)