from collections import Counter


def clear(kwargs):
    if (
        kwargs.get("shape") == "sphere"
        and kwargs.get("mass") <= 600
        and kwargs.get("mass") >= 300
        and kwargs.get("volume") <= 500
        and kwargs.get("volume") >= 100
    ):
        return 1
    return 0


def fruits(tuple_of_fruits):
    names = [i["name"] for i in tuple_of_fruits if clear(i)]
    return dict(Counter(names))


if __name__ == "__main__":
    print(fruits((
    {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})))
