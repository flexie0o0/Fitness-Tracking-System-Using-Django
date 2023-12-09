from django.urls import path 
from django.contrib import admin
from users import views
# from .views import streamlit_view

urlpatterns = [
    path('', views.LoginPage, name = 'login'),
    path('home/', views.HomePage, name = 'home'),
    # path('streamlit/', streamlit_view, name='streamlit_view'),
    path('home/workout/', views.WorkoutPage, name = 'workout'),
    path('home/profile/', views.ProfilePage, name = 'profile'),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
    path('admin/', admin.site.urls),
]
