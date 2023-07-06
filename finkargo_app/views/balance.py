from rest_framework.views import APIView
from finkargo_app.domain import BalanceDomain
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from finkargo_app.serializer import BalanceSerializer
from finkargo_app.use_cases.balance import BalanceUseCase


class BalanceView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = BalanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = BalanceDomain(**serializer.data)
        uc = BalanceUseCase()
        return uc.execute(domain=domain)
