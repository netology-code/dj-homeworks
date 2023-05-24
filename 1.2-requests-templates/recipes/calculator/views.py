from django.shortcuts import render

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

# def receipt(request, dish):
#     context = {}
#     context["recipe"] = DATA.get(dish, {})
#     return render(request, 'calculator/index.html', context=context)

def receipt(request, dish):
    try:
        pers = int(request.GET.get("servings", 1))
        if pers < 1:
            raise ValueError("Количество персон не может быть меньше одной")
    except:
        return render(request, 'calculator/index.html',
                      context={"recipe": {"Error": "Количество персон не может быть меньше одной"}})
    context = {"recipe": {}}
    for k, v in DATA.get(dish, {}).items():
        context["recipe"][k] = v * pers
    return render(request, 'calculator/index.html', context=context)