from django.urls import reverse
from django.test import Client
from finkargo_app.models import UserRegistration, UserData
import pytest


@pytest.mark.django_db()
def test_create_user_registration():
    user_registration = UserRegistration.objects.create(
        user='Brian_89',
        password='123456',
        create_date='12/08/2026'
    )
    assert user_registration.user == 'Brian_89'
    assert user_registration.password == '123456'

    user_registration = UserData.objects.create(
        name='Diego',
        last_name='Zapata',
        city='Medellín',
        cellphone='3127524936',
        registered_user=user_registration
    )
    assert user_registration.name == 'Diego'
    assert user_registration.last_name == 'Zapata'
    assert user_registration.city == 'Medellín'
    assert user_registration.cellphone == '3127524936'

# @pytest.mark.django_db()
# def test_login():
#     url = reverse('login')
#     data = {"username": "Brian", "password": "12345"}
#     response = Client().post(url, data=data, content_type='application/json')
#     assert response.status_code == 200
