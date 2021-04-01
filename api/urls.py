from django.urls import path
from api import views

urlpatterns = [
    path("login/", views.UserAPIView.as_view({"post": "user_login", "get": "get_user_count"})),
    path("register/", views.UserAPIView.as_view({"post": "user_register"})),

]
