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
from django.contrib import admin
from django.urls import path, re_path
from django.http import HttpRequest, HttpResponse, Http404


def home_page(request) -> HttpResponse:
    return HttpResponse("Main page")


def pass_page(request, password) -> HttpResponse:
    return HttpResponse(f"trufk {password}")


def pass_generate(request: HttpRequest, user_id) -> HttpResponse:
    # if user_id in users:
        return HttpResponse(f"user_id: {user_id}")



# /article/<article_id>/<article_slug> - буде повертати інформацію про статю: номер статі та ії залоговок (slug)
# /password/<password> - буде перевіряти переданий пароль: має містити букви латинського алфавіта у будь якому регістрі
# або цифри (інщі символи вважати забороненими), та бути завдовшки 8 символів.
# Виводи, чи відповідає переданий пароль цим параметрам, чи ні.
# /password/generate/<length> - буде відображати випадково сгенерований пароль заданої довжини

urlpatterns = [
    path('', home_page),
    path('home/', home_page),
    path('homepage/', home_page),
    path('article/<article_id>/<article_slug>/', home_page),
    path('password/<password>', pass_page),
    path('/password/generate/<length> ', pass_generate)
]
