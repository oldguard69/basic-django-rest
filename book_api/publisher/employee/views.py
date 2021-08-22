from rest_framework.viewsets import ModelViewSet
import django_filters

from .serializers import PublisherSerializer
from publisher.models import Publisher

class PublisherFilter(django_filters.FilterSet):
    name = django_filters.CharFilter('name', 'icontains')
    

class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = PublisherFilter