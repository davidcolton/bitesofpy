"""Tax Bracket Calculator

Here is the break-down on how much a US citizen's income was
taxed in 2019

      $0 - $9,700   10%
  $9,701 - $39,475  12%
 $39,476 - $84,200  22%
 $84,201 - $160,725 24%
$160,726 - $204,100 32%
$204,101 - $510,300 35%
$510,301 +          37%

For example someone earning $40,000 would
pay $4,658.50, not $40,000 x 22% = $8,800!

    9,700.00 x 0.10 =       970.00
   29,775.00 x 0.12 =     3,573.00
      525.00 x 0.22 =       115.50
----------------------------------
              Total =     4,658.50

More detail can be found here:
https://www.nerdwallet.com/blog/taxes/federal-income-tax-brackets/

Sample output from running the code in the if/main clause:

          Summary Report
==================================
 Taxable Income:        40,000.00
     Taxes Owed:         4,658.50
       Tax Rate:           11.65%

         Taxes Breakdown
==================================
    9,700.00 x 0.10 =       970.00
   29,775.00 x 0.12 =     3,573.00
      525.00 x 0.22 =       115.50
----------------------------------
              Total =     4,658.50
"""
from dataclasses import dataclass, field
from typing import List, NamedTuple

Bracket = NamedTuple("Bracket", [("end", int), ("rate", float)])
Taxed = NamedTuple("Taxed", [("amount", float), ("rate", float), ("tax", float)])

BRACKET = [
    Bracket(9_700, 0.1),
    Bracket(39_475, 0.12),
    Bracket(84_200, 0.22),
    Bracket(160_725, 0.24),
    Bracket(204_100, 0.32),
    Bracket(510_300, 0.35),
    Bracket(510_301, 0.37),
]


class Taxes:
    def __init__(self, income, bracket=BRACKET) -> None:
        self.income = income
        self.bracket = bracket
        self.tax_amounts = self._calculate_taxes()

    """Taxes class

    Given a taxable income and optional tax bracket, it will
    calculate how much taxes are owed to Uncle Sam.

    """

    def __str__(self) -> str:
        """Summary Report

        Returns:
            str -- Summary report

            Example:

                      Summary Report          
            ==================================
             Taxable Income:        40,000.00
                 Taxes Owed:         4,658.50
                   Tax Rate:           11.65%
        """
        ret_str = f"          Summary Report\n"
        ret_str += f"==================================\n"
        ret_str += f" Taxable Income: {self.income:16,.2f}\n"
        ret_str += f"     Taxes Owed: {self.taxes:16,.2f}\n"
        ret_str += f"       Tax Rate: {self.tax_rate:15.2f}% "

        return ret_str

    def report(self):
        """Prints taxes breakdown report"""
        ret_str = self.__str__()
        ret_str += "\n\n"
        ret_str += f"         Taxes Breakdown\n"
        ret_str += f"==================================\n"
        for tax in self.tax_amounts:
            ret_str += f"{tax.amount:12,.2f} x {tax.rate:0>.2f} = {tax.tax:12,.2f}\n"
        ret_str += f"----------------------------------\n"
        ret_str += f"              Total ={self.taxes:13,.2f}"

        print(ret_str)

    def _calculate_taxes(self):
        # What Brackets are applicable
        tax_brackets = []
        tax_amounts = []
        for brac in self.bracket:
            if brac.end < self.income:
                tax_brackets.append(brac)
            else:
                # Break after adding the first bracket that
                #   exceeds the bracket end
                tax_brackets.append(brac)
                break

        # Add each bracket tax amount to the tax_amount list
        start_tax = 0
        for tax_brac in tax_brackets:
            if tax_brac.end < self.income:
                tax_amounts.append(
                    Taxed(
                        tax_brac.end - start_tax,
                        tax_brac.rate,
                        round((tax_brac.end - start_tax) * tax_brac.rate, 2),
                    )
                )
                start_tax = tax_brac.end
            else:
                tax_amounts.append(
                    Taxed(
                        self.income - start_tax,
                        tax_brac.rate,
                        round((self.income - start_tax) * tax_brac.rate, 2),
                    )
                )

        return tax_amounts

    @property
    def taxes(self) -> float:
        """Calculates the taxes owed

        As it's calculating the taxes, it is also populating the tax_amounts list
        which stores the Taxed named tuples.

        Returns:
            float -- The amount of taxes owed
        """
        return sum(t.tax for t in self.tax_amounts)

    @property
    def total(self) -> float:
        """Calculates total taxes owed

        Returns:
            float -- Total taxes owed
        """
        return sum(t.tax for t in self.tax_amounts)

    @property
    def tax_rate(self) -> float:
        """Calculates the actual tax rate

        Returns:
            float -- Tax rate
        """
        return round((self.total / self.income) * 100, 2)


if __name__ == "__main__":
    income = 1_000_000
    t = Taxes(income)
    t.report()
