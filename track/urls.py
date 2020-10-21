from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, ChangeStatusViewSet, ReminderViewSet

#routers
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'changestatus', ChangeStatusViewSet, basename='changestatus')
router.register(r'reminder', ReminderViewSet, basename='reminder')

#url to API
urlpatterns = [
	path('api/', include(router.urls)),
	]
