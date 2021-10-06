from typing import Union, Dict, List

tree = {
    "node1": {
        "node11": {
            "node111": [1, 2, 3],
            "node112": [31, 5]
        },
        "node12": [31]
    },
    "node2": [7, 8, 9]
}


def collect_leaves(tree: Union[Dict, List]) -> List:
    if type(tree) is dict:
        result = []
        for element in tree.values():
            result.extend(collect_leaves(element))
        return result
    else:
        return tree

assert collect_leaves(tree) == [1, 2, 3, 31, 5, 31, 7, 8, 9]
assert collect_leaves([1, 2, 3]) == [1, 2, 3]