from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenVerifyView,TokenObtainPairView, TokenRefreshView
urlpatterns = [
    # path("notes/",views.users.as_view() ),
    path("signup/", views.SignUpView.as_view()),
    path("login/",views.Login.as_view() ),
    path("/token/refresh",TokenRefreshView.as_view() ),
    path("/token/verify",TokenVerifyView.as_view() ),
    path("logout/",views.Logout.as_view()),
    path("reset_password/",views.ResetPassword.as_view()),
    # path("/",views.ResetPassword.as_view()),
    # path("forget_password/",views.ResetPassword.as_view()),
    
]
