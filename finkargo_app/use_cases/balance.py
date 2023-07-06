from finkargo_app.domain import BalanceDomain
from rest_framework.views import Response


class BalanceUseCase:
    def execute(self, domain: BalanceDomain):
        # List with the months of the year.
        year_month = [
            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
            'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]
        # Verify that the names in the list of months are correct.
        for check_mmonth in domain.months:
            if check_mmonth not in year_month:
                error_message = {
                    "error_message": f"The word '{check_mmonth}' is not a month of the year"}
                return Response(
                    data=error_message,
                    status=400,
                    content_type="application/json"
                )
        # To make the balance sheet of each month
        balance_list = [
            {"month": month,
             "sales": domain.sales[domain.months.index(month)],
             "expenses": domain.expenses[domain.months.index(month)],
             "balance": domain.sales[domain.months.index(month)] -
                domain.expenses[domain.months.index(month)]}
            for month in domain.months
        ]
        return Response(data=balance_list)
