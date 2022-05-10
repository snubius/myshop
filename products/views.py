
from rest_framework import generics, response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializer import MovieSerializer
from rest_framework.permissions import IsAuthenficated

from .pagination import MoviePagination
from .permissions import IsAuthorOrReadOnly

from products.models import Movie


class MovieViewSet(ModelViewSet):
    pagination_class = MoviePagination
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        queryset = self.queryset
        name = request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data)

    @action(detail=False, methods=['get'])
    def filters(self, request, pk=None):
        queryset = self.queryset
        fr = request.query_params.get('fr')
        to = request.query_params.get('ro')
        if fr and to:
            queryset = queryset.filter(price__gte=fr, price__lte=to, )
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data)

    @action(detail=False, methods=['get'])
    def filters_years(self, request, pk=None):
        queryset = self.queryset
        year = request.query_params.get('year')

        if year:
            queryset = queryset.filter(year__year=year)
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data)