from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.Auth.as_view() )

]
