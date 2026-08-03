from django.urls import path, include
from . import views

urlpatterns = [
    path("notes/",views.users.as_view() )

]
