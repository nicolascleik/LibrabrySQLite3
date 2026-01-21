class Book:
    def __init__(self, title: str, writer: str, year: int, state_Read: bool):
        self.title = title
        self.writer = writer
        self.year = year
        self.state_Read = state_Read

    def __repr__(self):
        return f"Title: {self.title} | Writer: {self.writer} | Year: {self.year} | State: {self.state_Read}"