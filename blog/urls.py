from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path(
        'createbooking/', views.CreateBookingView.as_view(),
        name='createbooking'
        ),
    path(
        'managebooking/', views.ManageBookingView.as_view(),
        name='managebooking'
        ),
]