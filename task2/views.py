from django.shortcuts import render
from django.views.generic import TemplateView


def template_func(request):
    return render(request, "second_task/template_for_func.html")

class TemplateClass(TemplateView):
    template_name = "second_task/template_for_class.html"