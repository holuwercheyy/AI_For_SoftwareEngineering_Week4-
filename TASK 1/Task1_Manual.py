def sort_dict_list(dict_list, key):
    return sorted(dict_list, key=lambda x: x[key])

# Example:
dict_list = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 40}]
sorted_list = sort_dict_list(dict_list, 'age')
print(sorted_list)


