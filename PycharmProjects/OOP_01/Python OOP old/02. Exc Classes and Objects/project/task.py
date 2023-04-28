class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False
        self.comments = {}

    def change_name(self, new_name: str):
        if new_name == self.name:
            "Name cannot be the same."
        self.name = new_name

    def change_due_date(self, new_date: str):
        if new_date == self.due_date:
            "Date cannot be the same."
        self.due_date = new_date

    def add_comment(self, comment: str):
        if not self.comments:
            self.comments[1] = comment
        number_comment = len(self.comments)
        self.comments[number_comment + 1] = comment

    def edit_comment(self, comment_number: int, new_comment: str):
        if len(self.comments) >= comment_number:
            self.comments[comment_number] = new_comment
            result = ''
            quantity = len(self.comments)
            for comm in self.comments:
                quantity -= 1
                if not quantity == 0:
                    result += f"{comm}: {self.comments[comm]}, "
                else:
                    result += f"{comm}: {self.comments[comm]}"
            return result
        else:
            return "Cannot find comment."
