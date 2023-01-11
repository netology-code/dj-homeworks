DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
recipe_name ="Омлет"
recipe_ingredient = DATA['omlet']
print(recipe_ingredient)

recipe_ingredient_risult = {}
for ingredient, amount in recipe_ingredient.items():
    amount *= 2
    recipe_ingredient_risult[ingredient] = amount

context = dict(recipe=recipe_ingredient_risult, title = recipe_name)
print(context)

