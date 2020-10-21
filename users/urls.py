from django.urls import re_path, patterns
from .views import UserViewSet
 
urlpatterns = [
    re_path(r'^create/$', UserViewSet.as_view()),
]