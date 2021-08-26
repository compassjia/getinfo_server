from django.urls import path, re_path

from . import views


urlpatterns = [
    path('',views.Index.as_view()),
    path('query/',views.Query.as_view()),

    ]
