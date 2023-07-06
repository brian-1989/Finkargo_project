from finkargo_app.domain import (
    CreateUserDomain,
    UpdateUserDomain,
    DeleteUserDomain,
    CreateUserDataDomain
)
from finkargo_app.use_cases.user import (
    GetAllRegisteredUsers,
    CreateUserUseCase,
    UpdateUserUseCase,
    DeleteUserUseCase,
    GetAllUserDataUseCase,
    CreateUserDataUseCase,
    UpdateUserDataUseCase,
    DeleteUserDataUseCase
)
from finkargo_app.serializer import (
    LoginSerializer,
    UpdateUserSerealizer,
    DeleteUserSerealizer,
    CreateUserDataSerializer
)
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class GetAllUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        uc = GetAllRegisteredUsers()
        return uc.execute()


class CreateUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = CreateUserDomain(**serializer.data)
        uc = CreateUserUseCase()
        return uc.execute(domain=domain)


class UpdateUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request: Request):
        serializer = UpdateUserSerealizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = UpdateUserDomain(**serializer.data)
        uc = UpdateUserUseCase()
        return uc.execute(domain=domain)


class DeleteUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request):
        serializer = DeleteUserSerealizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = DeleteUserDomain(**serializer.data)
        uc = DeleteUserUseCase()
        return uc.execute(domain=domain)


class GetAllUserDataView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        uc = GetAllUserDataUseCase()
        return uc.execute()


class CreateUserDataView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = CreateUserDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = CreateUserDataDomain(**serializer.data)
        uc = CreateUserDataUseCase()
        return uc.execute(domain=domain)


class UpdateUserDataView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request: Request):
        serializer = UpdateUserSerealizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = UpdateUserDomain(**serializer.data)
        uc = UpdateUserDataUseCase()
        return uc.execute(domain=domain)


class DeleteUserDataView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request):
        serializer = DeleteUserSerealizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = DeleteUserDomain(**serializer.data)
        uc = DeleteUserDataUseCase()
        return uc.execute(domain=domain)
