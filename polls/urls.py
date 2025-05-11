from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.survey_create, name='survey_create'),
    path('survey/<int:pk>/', views.survey_detail, name='survey_detail'),
    path('survey/<int:pk>/vote/', views.survey_vote, name='survey_vote'),
    path('survey/<int:pk>/results/', views.survey_results, name='survey_results'),
]
