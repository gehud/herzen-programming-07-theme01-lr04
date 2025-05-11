from django.urls import path
from .views import SurveyAnalyticsListView, SurveyAnalyticsDetailView

urlpatterns = [
    path('surveys/', SurveyAnalyticsListView.as_view(), name='survey-analytics-list'),
    path('surveys/<int:pk>/', SurveyAnalyticsDetailView.as_view(), name='survey-analytics-detail'),
]
