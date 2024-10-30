from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice/', views.notice, name='notice'),
    path('notice/<int:id>', views.notice_detail, name='notice_detail'),
    path('notice-search/', views.notice_search, name='notice-search'),
]