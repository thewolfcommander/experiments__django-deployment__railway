from rest_framework.views import APIView, Response


class TestAPIView(APIView):
    def get(self, request):
        return Response({
            'status': 'ok'
        })