from django.urls import path
from . import views


urlpatterns = [
    path('', views.giggle_search, name='giggle_search'),
    path('history/', views.giggle_history, name='giggle_history'),
    path('delete/<int:pk>', views.delete_joke, name='delete_joke'),
]