from django.urls import path
from .  import views
from .views import UserRegisterView

urlpatterns = [
   path('register/', views.registerPage, name='register'),
   path('login/', views.loginPage, name='login'),
   
   #path('register/', UserRegisterView.as_view(), name='register'),
   
]
