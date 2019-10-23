from django.contrib import admin
from django.urls import path, include

from .views import BookmarkListView
from .views import BookmarkCreateView
from .views import BookmarkDetailView
from .views import BookmarkUpdateView
from .views import BookmarkDeleteView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('create/', BookmarkCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]
