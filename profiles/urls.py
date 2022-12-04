from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-csv', views.upload_csv, name='upload_csv'),
    path('upload-action/', views.upload_action, name='upload_action'),
    path('profile/<int:pk>', views.profile_detail, name='profile_detail'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
