#  . Flatten a nested list


def flatten_list(lst):

    flat = []

    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)

    return flat


print(flatten_list([1, [2, [3, 4], 5]]))