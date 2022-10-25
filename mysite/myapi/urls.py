from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views
'''from .views import (
    NoteApiView,
    NoteDetailApiView
)'''

'''router = routers.DefaultRouter()
router.register(r'notes', views.NoteViewSet)'''

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
'''urlpatterns = [
  path('notes/api', NoteApiView.as_view()),
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  path('notes/api/<int:id>/',NoteDetailApiView.as_view()),
]'''

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/new/', views.note_new, name='note_new'),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('accounts/', include('django.contrib.auth.urls')),
]
