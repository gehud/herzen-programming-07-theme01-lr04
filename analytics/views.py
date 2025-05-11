from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from polls.models import Survey
from .serializers import SurveySerializer
from .filters import SurveyFilter

class SurveyAnalyticsListView(generics.ListAPIView):
    serializer_class = SurveySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = SurveyFilter
    ordering_fields = ['created_at', 'responses__count']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = Survey.objects.prefetch_related(
            'questions',
            'questions__choices',
            'questions__answers'
        ).annotate_responses_count()

        # Additional filtering based on query parameters
        min_votes = self.request.query_params.get('min_votes')
        if min_votes is not None:
            queryset = queryset.filter(responses__count__gte=min_votes)

        max_votes = self.request.query_params.get('max_votes')
        if max_votes is not None:
            queryset = queryset.filter(responses__count__lte=max_votes)

        return queryset

class SurveyAnalyticsDetailView(generics.RetrieveAPIView):
    queryset = Survey.objects.prefetch_related(
        'questions',
        'questions__choices',
        'questions__answers'
    )
    serializer_class = SurveySerializer
    lookup_field = 'pk'
