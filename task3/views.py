from django.shortcuts import render


def card_page(request):
    title = "Корзина"
    text = "Извините, Ваша корзина пуста"
    context = {
        "title": title,
        "text": text,
    }
    return render(request, "third_task/card.html", context)


def games_page(request):
    title = "Игры"
    list_games = ["Пасьянс", "Паук", "Дурак", "Блэкджек"]
    context = {
        "title": title,
        "list_games": list_games,
    }
    return render(request, "third_task/games.html", context)


def platform_page(request):
    title = "Главная страница"
    texts = [
        {
            "slug": "platform",
            "text": "Главная",
        },
        {
            "slug": "games",
            "text": "Магазин",
        },
        {
            "slug": "card",
            "text": "Корзина",
        },
    ]
    context = {
        "title": title,
        "texts": texts,
    }
    return render(request, "third_task/platform.html", context)
