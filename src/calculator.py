import decimal
from decimal import Decimal

class Calculator:

    def __init__(self, items: list[Decimal]):
        self.items = items

    def calculate_sales_tax(self) -> Decimal:
        sub_total = self.get_sub_total()
        return sub_total * Decimal(sub_total)

    def get_sales_tax(self) -> Decimal:
        return Decimal(0.0775)

    def get_sub_total(self) -> Decimal:
        return Decimal(sum(self.items))

    def get_total(self) -> Decimal:
        return self.get_sub_total() + self.get_sales_tax()

if __name__ == "__main__":
    int_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    decimal_array = [Decimal(i) for i in int_array]
    total = Calculator(decimal_array).get_total()

    print(total)