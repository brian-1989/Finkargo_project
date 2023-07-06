from finkargo_app.domain import NumberMatrixDomain
from rest_framework.views import Response


class NumberMatrixUseCase:
    def execute(self, domain: NumberMatrixDomain):
        try:
            non_repeated_numbers = []
            repeated_numbers = []
            for number in domain.matrix:
                if number in non_repeated_numbers:
                    repeated_numbers.append(number)
                else:
                    non_repeated_numbers.append(number)
            non_repeated_numbers.sort()
            response = {
                "unclassified_matrix": domain.matrix,
                "Classified_matrix": non_repeated_numbers + repeated_numbers
            }
            return Response(data=response)
        except Exception as exc:
            error_message = {
                "error_message": exc.args}
            return Response(
                data=error_message,
                status=400,
                content_type="application/json"
            )
