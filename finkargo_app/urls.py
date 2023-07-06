from django.urls import path
from finkargo_app.views.balance import BalanceView
from finkargo_app.views.login import LoginView
from finkargo_app.views.number_matrix import NumberMatrix
from finkargo_app.views.user import (
    GetAllUserView,
    CreateUserView,
    UpdateUserView,
    DeleteUserView,
    GetAllUserDataView,
    CreateUserDataView,
    UpdateUserDataView,
    DeleteUserDataView
)

urlpatterns = [

]

urlpatterns += [
    path(
        'login/',
        LoginView.as_view(),
        name='login'),
    path(
        'number_matrix/',
        NumberMatrix.as_view(),
        name='number_matrix'),
    path(
        'balance/',
        BalanceView.as_view(),
        name='balance'),
    path(
        'get_all_users/',
        GetAllUserView.as_view(),
        name='get_all_user'),
    path(
        'create_user/',
        CreateUserView.as_view(),
        name='create_user'),
    path(
        'update_user/',
        UpdateUserView.as_view(),
        name='update_user'),
    path(
        'delete_user/',
        DeleteUserView.as_view(),
        name='delete_user'),
    path(
        'get_all_users_data/',
        GetAllUserDataView.as_view(),
        name='get_all_users_data'),
    path(
        'create_users_data/',
        CreateUserDataView.as_view(),
        name='create_users_data'),
    path(
        'update_users_data/',
        UpdateUserDataView.as_view(),
        name='update_users_data'),
    path(
        'delete_users_data/',
        DeleteUserDataView.as_view(),
        name='delete_users_data'),
]
