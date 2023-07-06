from finkargo_app.domain import NumberMatrixDomain
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from finkargo_app.serializer import NumberMatrixSerializer
from finkargo_app.use_cases.number_matrix import NumberMatrixUseCase


class NumberMatrix(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = NumberMatrixSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = NumberMatrixDomain(**serializer.data)
        uc = NumberMatrixUseCase()
        return uc.execute(domain=domain)
