import dataclasses
import datetime


@dataclasses.dataclass
class LoginDomain:
    user: str = None
    password: str = None


@dataclasses.dataclass
class NumberMatrixDomain:
    matrix: list = None


@dataclasses.dataclass
class BalanceDomain:
    months: list = None
    sales: list = None
    expenses: list = None


@dataclasses.dataclass
class CreateUserDomain:
    user: str = None
    password: str = None
    create_date: datetime.datetime = None


@dataclasses.dataclass
class UpdateUserDomain:
    user: str = None
    field: str = None
    value: str = None


@dataclasses.dataclass
class DeleteUserDomain:
    user: str = None


@dataclasses.dataclass
class CreateUserDataDomain:
    user: str = None
    name: str = None
    last_name: str = None
    city: str = None
    cellphone: int = 0
    registered_user: str = None
