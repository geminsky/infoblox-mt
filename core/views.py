from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filter
from core import serializers, models


class StandardResultsSetPagination(PageNumberPagination):
    """
    A class to override page number pagination
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UserDataAPI(ListAPIView):
    """
    List api to list the data
    url: api/all

    """
    serializer_class = serializers.UserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated,)
    queryset = models.Users.objects.all().order_by('-id')
    filter_backends = (filter.DjangoFilterBackend, )
    filterset_fields = ['data__enabled', ]

    def get(self, request, *args, **kwargs):

        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.pagination_class.page_size = int(request.GET.get('size', 10))
        return self.list(request, *args, **kwargs)


class UserDataAddAPI(ListCreateAPIView):
    """
    Post API for posting data
    url: api/new
    """
    serializer_class = serializers.UserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated,)
    queryset = models.Users.objects.all()
    filter_backends = (filter.DjangoFilterBackend, )
    filterset_fields = ['data__enabled', ]

    def get(self, request, *args, **kwargs):
        self.pagination_class.page_size = int(request.GET.get('size', 10))
        return self.list(request, *args, **kwargs)
