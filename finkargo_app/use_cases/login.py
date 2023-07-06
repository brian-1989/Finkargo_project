from datetime import datetime
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import Response
from finkargo_app.domain import LoginDomain
from finkargo_app.models import UserToken, UserRegistration
import pytz


class LoginUseCase:
    def execute(self, domain: LoginDomain):
        username = domain.user
        password = domain.password
        user_registration = UserRegistration.objects.filter(
            user=username).first()
        if not user_registration:
            error_message = {
                "error_message": f"The '{username}' does not exist"}
            return Response(
                data=error_message,
                status='400', content_type='application/json')
        if user_registration.password != password:
            error_message = {
                "error_message": "Incorrect password"}
            return Response(
                data=error_message,
                status='400', content_type='application/json')
        user = User.objects.filter(username=username).first()
        if not user:
            User.objects.create(username=username, password=password)
            user = User.objects.filter(username=username).first()
        token = Token.objects.filter(user=user).first()
        if token:
            token.delete()
        new_token = Token.objects.create(user=user)
        try:
            get_user_instance = UserRegistration.objects.get(
                user=user)
            date = datetime.now(tz=pytz.timezone(
                'America/Bogota')).strftime("%Y/%m/%d, %H:%M:%S")
            UserToken.objects.create(
                registered_user=get_user_instance,
                token=new_token,
                create_date=date.split(',')[0])
        except BaseException:
            get_token = UserToken.objects.get(registered_user=user)
            get_token.token = new_token
            get_token.save()
        return Response({"token": str(new_token)})
