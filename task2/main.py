import csv
import timeit
from BTrees.OOBTree import OOBTree

def load_data_from_csv(filename):
    items = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append({
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"])
            })
    return items

#tree
def add_item_to_tree(tree, item):
    tree[item["ID"]] = item

def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items(min_price, max_price)]

def simple_range_query_tree(tree, min_price, max_price):
    return [item for item in tree.values() if min_price <= item["Price"] <= max_price]

#dict
def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = item

def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item["Price"] <= max_price]

#measure
def measure_performance(structure, query_func, min_price, max_price, query_amount):
    return timeit.timeit(lambda: query_func(structure, min_price, max_price), number=query_amount)


def main():
    filename = "./task2/generated_items_data.csv"
    csv_items = load_data_from_csv(filename)

    tree = OOBTree()
    dictionary = {}

    for item in csv_items:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    # Change the query parameters if needed
    min_price, max_price = 50, 200
    query_amount = 100

    time_tree = measure_performance(tree, range_query_tree, min_price, max_price, query_amount)
    print(f"Total range_query time for OOBTree: {time_tree:.6f} seconds")

    time_s_tree = measure_performance(tree, simple_range_query_tree, min_price, max_price, query_amount)
    print(f"Total simple range_query time for OOBTree: {time_s_tree:.6f} seconds")

    time_dict = measure_performance(dictionary, range_query_dict, min_price, max_price, query_amount)
    print(f"Total range_query time for Dict: {time_dict:.6f} seconds")

if __name__ == "__main__":
    main()