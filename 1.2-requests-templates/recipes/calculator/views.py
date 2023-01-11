from django.shortcuts import render
from django.urls import reverse

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

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view(request):
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }
    
    context = {
        'pages': pages
    }
    return render(request, 'calculator/index0.html', context)

def omlet_view(request):
    context = get_context(request, 'omlet', "Омлет")
    return render(request, 'calculator/index.html', context)

def pasta_view(request):
    context = get_context(request, 'pasta', "Паста")
    return render(request, 'calculator/index.html', context)

def buter_view(request):
    context = get_context(request, 'buter', "Бутерброд")
    return render(request, 'calculator/index.html', context)

def get_context(request, recipe_name, recipe_name_rus):
    servings = int(request.GET.get("servings", 1))

    recipe_ingredient = DATA[recipe_name]
    recipe_ingredient_risult = {}

    for ingredient, amount in recipe_ingredient.items():
        amount *= servings
        recipe_ingredient_risult[ingredient] = round(amount, 2) 
    
    context = dict(recipe=recipe_ingredient_risult, title = recipe_name_rus)

    return context