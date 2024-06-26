from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('person', views.person, name="person"),
    path('logout', views.logout_view, name="logout"),
]