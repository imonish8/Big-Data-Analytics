def item_frequency_simple(purchased_items):
    for item in set(purchased_items):
        print(f"{item}: {purchased_items.count(item)}")

purchased_items = ["apple", "banana", "orange", "apple", "banana", "kiwi", "orange", "apple"]
item_frequency_simple(purchased_items)