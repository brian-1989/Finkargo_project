from finkargo_app.models import UserRegistration
import pytest

@pytest.mark.django_db
def test_create_user_registration():
    user_registration = UserRegistration.objects.create(
        user='Brian_89',
        password='123456',
        create_date='12/08/2026'
    )
    assert user_registration.user == 'Brian_89'