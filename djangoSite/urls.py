"""djangoSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import random
import string

from django.contrib import admin
from django.urls import path, re_path
from django.http import HttpRequest, HttpResponse, Http404


def home_page(request) -> HttpResponse:
    return HttpResponse("Main page")


def article_page(request, article_id, article_slug) -> HttpResponse:
    return HttpResponse(f"Article {article_id} <h1>{article_slug}</h1")


def pass_page(request, password) -> HttpResponse:
    letters = string.ascii_letters
    digits = string.digits
    if len(password) != 8:
        return HttpResponse(f"Password not correct: must have 8 symbols")
    for chr_in_pass in password:
        if chr_in_pass not in letters and chr_in_pass not in digits:
            return HttpResponse(f"Password not correct: may include only "
                                f"small, capital latin symbols or digits ")
    return HttpResponse(f"Password is correct")


def pass_generate(request, length) -> HttpResponse:
    pass_symbols = string.ascii_letters + string.digits
    password = random.sample(pass_symbols, length)
    return HttpResponse(password)


# /article/<article_id>/<article_slug> - буде повертати інформацію про статю: номер статі та ії залоговок (slug)
# /password/<password> - буде перевіряти переданий пароль: має містити букви латинського алфавіта у будь якому регістрі
# або цифри (інщі символи вважати забороненими), та бути завдовшки 8 символів.
# Виводи, чи відповідає переданий пароль цим параметрам, чи ні.
# /password/generate/<length> - буде відображати випадково сгенерований пароль заданої довжини


urlpatterns = [
    path('', home_page),
    path('home/', home_page),
    path('homepage/', home_page),
    path('article/<int:article_id>/<slug:article_slug>/', article_page),
    path('password/<str:password>/', pass_page),
    path('password/generate/<int:length>/', pass_generate),
]
