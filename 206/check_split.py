from decimal import Decimal
from decimal import ROUND_DOWN


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    total = Decimal(item_total[1:])
    tax_percent = Decimal(tax_rate[:-1]) / 100
    tip_percent = Decimal(tip[:-1]) / 100

    total_plus_tax = (total + total * tax_percent).quantize(Decimal(".01"))
    total_plus_tip = (total_plus_tax + total_plus_tax * tip_percent).quantize(
        Decimal(".01")
    )

    cost_per_person = (total_plus_tip / people).quantize(
        Decimal(".01"), rounding=ROUND_DOWN
    )
    list_of_splits = [cost_per_person] * people

    if total_plus_tip != sum(list_of_splits):
        diff = (total_plus_tip - sum(list_of_splits)).quantize(Decimal(".01"))

        pay_extra = 0
        while diff > 0:
            list_of_splits[pay_extra] += Decimal(0.01)
            diff -= Decimal(0.01)
            pay_extra += 1
    print(total_plus_tip, list_of_splits)
    return f"${total_plus_tip:.2f}", list_of_splits
