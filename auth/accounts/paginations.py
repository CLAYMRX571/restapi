from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 199

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = '-created_at'
    cursor_query_param = 'page'

class CustomPagination(PageNumberPagination):
    page_size = 199
    page_size_query_param = 'page_size'
    max_page_size = 199

    def paginate_queryset(self, queryset, request, view=None):
       page_size = int(request.query_params.get('page_size', 10))
       page = int(request.query_params.get('page', 1))
       offset = (page - 1) * page_size
       return queryset[offset:offset + page_size]

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data 
        })