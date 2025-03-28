from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index),
    path("submit", views.submit),
    path("post", views.post_data),
    path("get", views.fetch_data)
]