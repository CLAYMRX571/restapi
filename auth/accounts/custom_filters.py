from accounts.models import Article
import django_filters

class CustomArticleFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    search = django_filters.CharFilter(method='filter_by_search')

    def filter_by_search(self, queryset, name, value):
        return queryset.filter(title__icontains=value) | queryset.filter(author__first_name__icontains=value)

    class Meta:
        model = Article
        fields = ['author', 'min_price', 'max_price', 'search']