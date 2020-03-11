from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from ...serializers.product_serializer import ProductSerializer
from ...models.product import Product
from rest_framework.views import APIView


from rest_framework.pagination import PageNumberPagination
import math

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'total_count': self.page.paginator.count,
            'page_size': self.page_size,
            'page_count': math.ceil(self.page.paginator.count / self.page_size),
            'current_page': self.page.number,
            'next_link': self.get_next_link(),
            'previous_link': self.get_previous_link(),
            'results': data,
        })


class ProductListView(APIView):
   def post(self, request):
        data = request.data
        print(data)
        try:
           return Response(data  )
        except:
            return Response(dict(error="I couldn't get valid data"), status=status.HTTP_400_BAD_REQUEST)
