def get_unique_items(data):
    unique_list = []
    seen = set()

    for value in data:
        if value not in seen:
            unique_list.append(value)
            seen.add(value)

    return unique_list


def count_elements(data):
    result = {}

    for value in data:
        result[value] = result.get(value, 0) + 1

    return result


def swap_dict_keys_values(dictionary):
    new_dict = {}

    for k in dictionary:
        v = dictionary[k]
        new_dict[v] = k

    return new_dict
