from . import views
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]