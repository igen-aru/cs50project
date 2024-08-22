def get_calories(fruit):
    fruits_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 105,
        "blueberries": 85,
        "cantaloupe": 50,
        "grapefruit": 52,
        "grapes": 62,
        "honeydew melon": 61,
        "kiwifruit": 90,
        "lemon": 17,
        "lime": 20,
        "nectarine": 62,
        "orange": 62,
        "peach": 59,
        "pear": 100,
        "pineapple": 50,
        "plums": 30,
        "strawberries": 4,
        "sweet cherries": 100,
        "tangerine": 47,
        "watermelon": 85
    }
    fruit = fruit.lower()
    return fruits_calories.get(fruit)

def main():
    fruit = input("Item: ").strip()

    calories = get_calories(fruit)
    if calories is not None:
        print(f"{calories}")
    else:
        print("")
main()
