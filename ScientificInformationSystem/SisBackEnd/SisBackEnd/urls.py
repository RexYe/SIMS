
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'get_authors_by_name$', views.get_authors_by_name)
]
