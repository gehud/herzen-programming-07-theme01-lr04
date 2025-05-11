import django_filters
from polls.models import Survey

class SurveyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    min_votes = django_filters.NumberFilter(method='filter_min_votes')
    max_votes = django_filters.NumberFilter(method='filter_max_votes')

    class Meta:
        model = Survey
        fields = ['title', 'created_at']

    def filter_min_votes(self, queryset, name, value):
        return queryset.filter(responses__count__gte=value)

    def filter_max_votes(self, queryset, name, value):
        return queryset.filter(responses__count__lte=value)
