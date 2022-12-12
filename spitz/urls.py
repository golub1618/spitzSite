from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("types/", types, name="types"),
    path("login/", login, name="login"), 
    path("type/<int:type_id>/", show_type, name="type")
]