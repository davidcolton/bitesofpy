from abc import ABC, abstractmethod


class Challenge(ABC):
    def __init__(self, number, title):
        self.number = number
        self.title = title
        super().__init__()

    @abstractmethod
    def verify(self):
        pass

    @property
    @abstractmethod
    def pretty_title(self):
        pass


class BlogChallenge(Challenge):
    def __init__(self, number, title, merged_prs):
        self.merged_prs = merged_prs
        super().__init__(number, title)

    def verify(self, blog_challenge):
        return blog_challenge in self.merged_prs

    @property
    def pretty_title(self):
        return f"PCC1 - {self.title}"


class BiteChallenge(Challenge):
    def __init__(self, number, title, result):
        self.result = result
        super().__init__(number, title)

    def verify(self, result):
        return self.result.strip().lower() == result.strip().lower()

    @property
    def pretty_title(self):
        return f"Bite 24. {self.title}"
