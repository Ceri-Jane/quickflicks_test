from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import profile, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
]
