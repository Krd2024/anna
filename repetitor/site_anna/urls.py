from django.urls import path
from django.conf.urls import handler404, handler400

# from .views import *
from .views import *
from .auth import auth_user_view

urlpatterns = [
    path("", index, name="index"),
    path("ege/", index_ege, name="index_ege"),
    path("about_me/", about_me, name="about_me"),
    path("advantages/", advantages, name="advantages"),
    path("education/", education, name="education"),
    path("contact/", contact, name="contact"),
    path("materials/", materials, name="materials"),
    path("price/", price, name="price"),
    path("faq/", faq, name="faq"),
    #
    path("review/", review, name="review"),
    #
    path("signup/", auth_user_view.signup, name="signup"),
    path(
        "account_activation_sent/",
        auth_user_view.account_activation_sent,
        name="account_activation_sent",
    ),
    path("activate/<uidb64>/<token>/", auth_user_view.activate, name="activate"),
    #
    path("pdf/", pdf_list, name="pdf_list"),
    #
    path("login_in/", auth_user_view.login_in, name="login_in"),
    path("login/", auth_user_view.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_user_view.logoutPage, name="logout"),
]
