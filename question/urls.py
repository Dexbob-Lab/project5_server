from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('question/', views.question, name='question'),
    path('question/<int:id>/', views.question_detail, name='question-detail'),
    path('question-search/', views.question_search, name='question-search'),
    path('question-password/', views.question_password, name='question-password'),
    path('question-hits/<int:id>/', views.question_hits, name='question-hits'),
]