from . import views
from django.urls import path


urlpatterns = [
    path('', Indexview.as_view(), name='home'),
]