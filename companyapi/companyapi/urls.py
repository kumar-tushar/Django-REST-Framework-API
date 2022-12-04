from django.contrib import admin
from django.urls import path, include
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page),
    path('api/', include('api.urls')),
]
