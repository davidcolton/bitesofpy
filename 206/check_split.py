import math


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    total_float = float(item_total[1:])
    tax_rate_float = float(tax_rate[:-1]) / 100
    tip_float = float(tip[:-1]) / 100

    total_plus_tax = round(total_float + total_float * tax_rate_float, 2)
    total_plus_tip = round(total_plus_tax + total_plus_tax * tip_float, 2)

    cost_per_person = math.floor((total_plus_tip / people) * 100) / 100
    list_of_splits = [cost_per_person] * people

    if total_plus_tip != sum(list_of_splits):
        diff = round(total_plus_tip - sum(list_of_splits), 2)
        pay_extra = 0
        while diff > 0:
            list_of_splits[pay_extra] += 0.01
            diff -= 0.01
            pay_extra += 1
    return f"${total_plus_tip:.2f}", list_of_splits
