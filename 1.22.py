def avg(x):
    return sum(x)/len(x)


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


list1 = [1, 2, 3, 4, 5, 10]
print(drop_first_last(list1))
