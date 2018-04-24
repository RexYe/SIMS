from django.urls import path
from . import views
urlpatterns = [
    path('get_authors_by_name', views.get_authors_by_name,)
]