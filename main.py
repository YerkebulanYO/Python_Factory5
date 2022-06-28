from random import randint


# TASK #1
def func(input_list, k):
    total = []

    if len(input_list) <= k:
        return input_list

    for _ in range(k):
        number = randint(0, len(input_list) - 1)
        total.append(input_list.pop(number))

    return total


# TASK #2
def new_func(input_list, prob, k):
    total = []

    if len(input_list) <= k:
        return input_list

    for _ in range(k):
        while True:
            index = randint(0, len(input_list) - 1)

            p = randint(0, 9)
            if prob[index] >= p:
                total.append(input_list.pop(index))
                break

    return total
