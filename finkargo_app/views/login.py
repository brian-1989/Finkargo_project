from finkargo_app.domain import LoginDomain
from rest_framework.views import APIView
from rest_framework.request import Request
from finkargo_app.serializer import LoginSerializer
from finkargo_app.use_cases.login import LoginUseCase


class LoginView(APIView):

    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = LoginDomain(**serializer.data)
        uc = LoginUseCase()
        return uc.execute(domain=domain)
