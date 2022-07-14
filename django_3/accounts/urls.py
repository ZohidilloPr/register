from django.urls import path
from .views import CreateUser

app_name = 'accounts'

urlpatterns = [
    path("signup/", CreateUser, name="CU")
]
