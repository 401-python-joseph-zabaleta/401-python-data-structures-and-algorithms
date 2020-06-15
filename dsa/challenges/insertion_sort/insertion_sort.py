def insertion_sort(list1):
    for i in range(1, len(list1)):
        j = i - 1
        temp = list1[i]

        while j >= 0 and temp < list1[j]:
            list1[j + 1] = list1[j]
            j = j - 1

            list1[j + 1] = temp

    return list1
