from django.shortcuts import render


def card_page(request):
    pagename = "Корзина"
    text = "Извините, Ваша корзина пуста"
    context = {
        "pagename": pagename,
        "text": text,
    }
    return render(request, "fourth_task/card.html", context)


def games_page(request):
    pagename = "Игры"
    list_games = {
        "games": ["Пасьянс", "Паук", "Дурак", "Блэкджек"]
    }
    context = {
        "pagename": pagename,
        "list_games": list_games,
    }
    return render(request, "fourth_task/games.html", context)


def platform_page(request):
    pagename = "Главная страница"
    context = {
        "pagename": pagename,
    }
    return render(request, "fourth_task/platform.html", context)
