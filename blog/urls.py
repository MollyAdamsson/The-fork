from . import views
from .views import EditBookingView
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
    path(
        'editbooking/<int:pk>/', views.EditBookingView.as_view(),
        name='editbooking'
        ),
    path(
        'bookingsuccess/', views.BookingSuccessView.as_view(),
        name='bookingsuccess'
        ),
    path(
        'deletebooking/', views.DeleteBookingView.as_view(),
        name='deletebooking'
        ),
    path(
        'deletesuccess/', views.DeleteSuccessView.as_view(),
        name='deletesuccess'
        ),
]
