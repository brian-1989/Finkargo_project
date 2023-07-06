from datetime import datetime
from finkargo_app.domain import (
    CreateUserDomain,
    UpdateUserDomain,
    DeleteUserDomain,
    CreateUserDataDomain
)
from finkargo_app.models import UserRegistration, UserData
from rest_framework.views import Response
import pytz


class GetAllRegisteredUsers:
    def execute(self):
        get_all_users = UserRegistration.objects.all().values()
        user_list = [user for user in get_all_users]
        return Response(data=user_list)


class CreateUserUseCase:
    def execute(self, domain: CreateUserDomain):
        # Check if the user is registered
        check_user = UserRegistration.objects.filter(user=domain.user)
        if list(check_user) != []:
            error_message = {
                "error_message": f"The '{domain.user}' user is already registered"}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
        # Create user registration
        date = datetime.now(tz=pytz.timezone('America/Bogota')
                            ).strftime("%Y/%m/%d, %H:%M:%S")  # "%m/%d/%Y"
        domain.create_date = date.split(',')[0]
        user_store = UserRegistration(**domain.__dict__)
        user_store.save()
        return Response(data={"status": "Done"})


class UpdateUserUseCase:
    def execute(self, domain: UpdateUserDomain):
        # Check if the user is registered
        check_user = UserRegistration.objects.filter(user=domain.user).first()
        if not check_user:
            error_message = {
                "error_message": f"The '{domain.user}' user to update does not exist"}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
        # Update user registration
        if domain.field == 'user':
            check_user.user = domain.value
        elif domain.field == 'password':
            check_user.password = domain.value
        else:
            error_message = {
                "error_message": f"The '{domain.field}' field to update does not exist"}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
        check_user.save()
        message = {
            "message": f"The {domain.field} field has been update by {domain.value}"}
        return Response(data=message)


class DeleteUserUseCase:
    def execute(self, domain: DeleteUserDomain):
        # Check if the user is registered
        check_user = UserRegistration.objects.filter(user=domain.user).first()
        if not check_user:
            error_message = {
                "error_message": f"The '{domain.user}' user to delete does not exist"}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
        # Delete user registration
        check_user.delete()
        message = {
            "message": f"The {domain.user} user was deleted"}
        return Response(data=message)


class GetAllUserDataUseCase:
    def execute(self):
        get_all_users_data = UserData.objects.all().values()
        user_list = [user for user in get_all_users_data]
        return Response(data=user_list)


class CreateUserDataUseCase:
    def execute(self, domain: CreateUserDataDomain):
        # Check if the user is registered
        check_user_registration = UserRegistration.objects.filter(
            user=domain.user).first()
        if not check_user_registration:
            error_message = {
                "error_message": f"The '{domain.user}' user is already registered"}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
        id_user_registration = check_user_registration.id
        # checks whether the user's data is registered
        check_user_data = UserData.objects.filter(
            registered_user=id_user_registration).first()
        if check_user_data:
            error_message = {
                "error_message": f"The '{domain.name}' user is already registered the data"}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
        # Create user data
        get_user_instance = UserRegistration.objects.get(user=domain.user)
        domain.registered_user = get_user_instance
        domain.__dict__.pop('user')
        user_store = UserData(**domain.__dict__)
        user_store.save()
        return Response(data={"status": "Done"})


class UpdateUserDataUseCase:
    def execute(self, domain: UpdateUserDomain):
        # Check if the user is registered
        check_user_registration = UserRegistration.objects.filter(
            user=domain.user).first()
        if not check_user_registration:
            error_message = {
                "error_message": f"The '{domain.user}' user is not registered"}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
        id_user_registration = check_user_registration.id
        # checks whether the user's data is registered
        check_user_data = UserData.objects.filter(
            registered_user=id_user_registration).first()
        if not check_user_data:
            error_message = {
                "error_message": "This user has no registered data"}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
        # Update user data
        if domain.field == 'name':
            check_user_data.name = domain.value
        elif domain.field == 'last_name':
            check_user_data.password = domain.value
        elif domain.field == 'city':
            check_user_data.city = domain.value
        elif domain.field == 'cellphone':
            check_user_data.cellphone = domain.value
        else:
            error_message = {
                "error_message": f"The '{domain.field}' field to update does not exist"}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
        check_user_data.save()
        message = {
            "message": f"The {domain.field} field has been update by {domain.value}"}
        return Response(data=message)


class DeleteUserDataUseCase:
    def execute(self, domain: DeleteUserDomain):
        # Check if the user is registered
        check_user_registration = UserRegistration.objects.filter(
            user=domain.user).first()
        if not check_user_registration:
            error_message = {
                "error_message": f"The '{domain.user}' user is already registered"}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
        id_user_registration = check_user_registration.id
        # checks whether the user's data is registered
        check_user_data = UserData.objects.filter(
            registered_user=id_user_registration).first()
        if not check_user_data:
            error_message = {
                "error_message": "This user has no registered data"}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
        # Delete user data
        check_user_data.delete()
        message = {
            "message": f"{domain.user}'s user data was deleted"}
        return Response(data=message)
