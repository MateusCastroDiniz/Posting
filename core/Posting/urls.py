from django.urls import path
from core.Posting import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]
