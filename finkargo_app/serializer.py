from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    user = serializers.CharField(
        allow_blank=False, required=True, max_length=100)
    password = serializers.CharField(
        allow_blank=False, required=True, max_length=100)


class NumberMatrixSerializer(serializers.Serializer):
    matrix = serializers.ListField()


class BalanceSerializer(serializers.Serializer):
    months = serializers.ListField(
        child=serializers.CharField(allow_blank=False, required=True)
    )
    sales = serializers.ListField(
        child=serializers.IntegerField()
    )
    expenses = serializers.ListField(
        child=serializers.IntegerField()
    )


class UpdateUserSerealizer(serializers.Serializer):
    user = serializers.CharField(
        allow_blank=False, required=True, max_length=100)
    field = serializers.CharField(
        allow_blank=False, required=True, max_length=100)
    value = serializers.CharField(
        allow_blank=False, required=True, max_length=100)


class DeleteUserSerealizer(serializers.Serializer):
    user = serializers.CharField(
        allow_blank=False, required=True, max_length=100)


class CreateUserDataSerializer(serializers.Serializer):
    user = serializers.CharField(
        allow_blank=False, required=True, max_length=100)
    name = serializers.CharField(
        allow_blank=False, required=True, max_length=100)
    last_name = serializers.CharField(
        allow_blank=False, required=True, max_length=100)
    city = serializers.CharField(
        allow_blank=False, required=True, max_length=100)
    cellphone = serializers.IntegerField()
