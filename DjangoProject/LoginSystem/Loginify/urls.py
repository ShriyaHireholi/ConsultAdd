from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("get_users", views.get_users, name="get_users"),
    path("update_user/<username>/", views.update_user, name="update_user"),
    path("delete_user", views.delete_user, name="delete_user"),
]