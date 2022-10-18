from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import (
    NoteApiView,
)

router = routers.DefaultRouter()
router.register(r'notes', views.NoteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
  path('notes/api', NoteApiView.as_view()),
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]