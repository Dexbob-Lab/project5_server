from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice/', views.notice, name='notice'),
    path('notice/<int:id>/', views.notice_detail, name='notice-detail'),
    path('notice-search/', views.notice_search, name='notice-search'),
    path('notice-password/', views.notice_password, name='notice-password'),
    path('notice-hits/<int:id>/', views.notice_hits, name='notice-hits'),
]