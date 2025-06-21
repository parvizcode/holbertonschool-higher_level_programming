# 1-search_replace.py

def search_replace(my_list, search, replace):
    return [replace if x == search else x for x in my_list]
