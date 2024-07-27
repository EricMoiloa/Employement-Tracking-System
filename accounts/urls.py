from django.urls import path,include
from accounts import views
urlpatterns = [
    
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),  
]
