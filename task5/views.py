from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import UserRegister


def sign_up_by_django(request: HttpRequest):
    users = ['alex', 'oleg', 'anna', 'tolik', 'john']
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            # получаю данные
            error = None
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]
            # обрабатываю данные
            if password != repeat_password:
                error = "Пароли не совпадают."
            elif age < 18:
                error = "Вы должны быть старше 18."
            elif username in users:
                error = "Пользователь уже существует"
            else:
                info["text"] = f"Приветствуем, {username}!"
            info["error"] = error
            info["form"] = form
    else:
        info["form"] = UserRegister()
    return render(request=request, context=info, template_name="fifth_task/registration_page.html")


def sign_up_by_html(request: HttpRequest):
    users = ['alex', 'oleg', 'anna', 'tolik', 'john']
    info = {}
    if request.method == "POST":
        # получаю данные
        error = None
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        # обрабатываю данные
        if password != repeat_password:
            error = "Пароли не совпадают."
        elif int(age) < 18:
            error = "Вы должны быть старше 18."
        elif username in users:
            error = "Пользователь уже существует"
        else:
            info["text"] = f"Приветствуем, {username}!"
        info["error"] = error
        return render(request, context=info, template_name="fifth_task/registration_page.html")
    else:
        return render(request, "fifth_task/registration_page.html")
