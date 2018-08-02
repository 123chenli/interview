def quicksort(list):
    if len(list) < 2:
        return list
    else:
        mid = list[0]
        lessbeforemid = [i for i in list[1:] if i <= mid]
        biggerafter = [i for i in list[1:] if i > mid]
        finallylist = quicksort(lessbeforemid)+[mid]+quicksort(biggerafter)
        return finallylist

print(quicksort([2, 4, 6, 7, 1, 2, 5]))