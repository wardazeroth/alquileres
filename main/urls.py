from django.urls import path
from main.views import indexView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    
    path('login/', LoginView.as_view(), name= 'login_url'),
    path('login/', LogoutView.as_view(next_page= 'home'), name= 'logout')
]