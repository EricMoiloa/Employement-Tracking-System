from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('success/',views.success,name='success'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('adminside/',views.adminside,name='adminside'),
    path('doctors/',views.doctors,name='doctors'),
    path('patients/',views.patients,name='patients'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('admin_login/',views.admin_login,name='admin_login'),
]
