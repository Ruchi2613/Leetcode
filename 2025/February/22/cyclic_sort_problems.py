def cyclic_sort(n):
    for i in range(len(n)):
        correct_ind = n[i] - 1
        if correct_ind != i:
            n[i], n[correct_ind] = n[correct_ind], n[i]

    return n
print(cyclic_sort(n=[3, 1, 5, 4, 2]))
