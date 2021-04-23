import django_filters
from django_filters import DateFilter
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    choice_day = tuple((x, x) for x in range(1, 32))
    choice_month = tuple((x, x) for x in range(1, 13))
    day = django_filters.ChoiceFilter(field_name="published_date",lookup_expr='day',label="Day",choices=choice_day)
    month = django_filters.ChoiceFilter(field_name='published_date', lookup_expr='month', label="Month",choices=choice_month)
    year = django_filters.NumberFilter(field_name='published_date', lookup_expr='year', label="Year")

    class Meta:
        model = Book
        fields = ['title','author']    