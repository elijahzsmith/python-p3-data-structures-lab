spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass
    # names = []
    # for food in spicy_foods:
    #     print(food["name"])
    #     names.append(food["name"])
    
    # return names
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    pass
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    pass
    spicy_list = []
    for food in spicy_foods:
        sentence = f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}'
        print(sentence)
        spicy_list.append(sentence)

    return spicy_list

def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if (food["cuisine"] == cuisine):
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if (food['heat_level'] > 5):
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')


def get_average_heat_level(spicy_foods):
    heat_levels = [food['heat_level'] for food in spicy_foods]
    return (sum(heat_levels) / len(heat_levels))

