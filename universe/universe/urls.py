from django.contrib import admin
from django.urls import path, include
import re

urlpatterns = [
    path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
