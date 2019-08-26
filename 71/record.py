class RecordScore:
    """Class to track a game's maximum score"""

    def __init__(self):
        self.record = 0

    def __call__(self, record):
        if self.record < record:
            self.record = record
        return self.record
