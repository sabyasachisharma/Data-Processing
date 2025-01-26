from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.file_upload, name='file_upload'),  # File upload route
    path('dashboard/', views.file_dashboard, name='file_dashboard'),  # Dashboard route
    path('download/<int:file_id>/', views.file_download, name='file_download'),  # File download route
]
