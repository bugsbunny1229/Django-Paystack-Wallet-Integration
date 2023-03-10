from django.urls import path
from .views import Login, Register


urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
]