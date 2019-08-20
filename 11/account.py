class Account:
    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # Adding to balance
    def __add__(self, amount):
        try:
            self._transactions.append(int(amount))
        except ValueError:
            raise

    # Subtracting from balance
    def __sub__(self, amount):
        try:
            self._transactions.append(-int(amount))
        except ValueError:
            raise

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, indexOrSlice):
        try:
            return self._transactions[indexOrSlice]
        except TypeError:
            raise

    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"

