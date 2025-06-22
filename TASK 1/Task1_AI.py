def sort_dict_list(dict_list, key):
    try:
        return sorted(dict_list, key=lambda x: x[key])
    except KeyError:
        print(f"Error: Key '{key}' not found in dictionary.")
        return []

# Example:
dict_list = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 40}]
sorted_list = sort_dict_list(dict_list, 'age')
print(sorted_list)

