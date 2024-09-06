from collections import defaultdict
from typing import List, Dict


def merge_items(items: List[dict]) -> Dict[str, int]:
    merged_items = defaultdict(int)  # Initial value of each key is 0
    for item in items:
        merged_items[item["item"]] += item["amount"]
    return merged_items


if __name__ == '__main__':
    items = [{"item": "item1", "amount": 400},
             {"item": "item2", "amount": 300},
             {"item": "item1", "amount": 750}]

    merged_items = merge_items(items=items)
    print(merged_items)

counter = {}
for item in items:
    value = list(item.values())
    print(value)
    if value[0] in list(counter.keys()):
        counter[value[0]] = value[1] + counter[value[0]]
    else:
        counter[value[0]] = value[1]

print(counter)
