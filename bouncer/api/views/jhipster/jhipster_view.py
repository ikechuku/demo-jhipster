from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class JhipsterView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        try:
           return Response(data  )
        except:
            return Response(dict(error="I couldn't get valid data"), status=status.HTTP_400_BAD_REQUEST)
