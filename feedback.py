class Feedback:
    def __init__(self, date="No Date", text="No Text", student=None, tutor=None):
        self._date = date
        self._text = text
        self._student = student
        self._tutor = tutor

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not value:
            raise ValueError("Text cannot be empty")
        self._text = value

    def set_data(self, date, text, student, tutor):
        self._date = date
        self.text = text
        self._student = student
        self._tutor = tutor

    def __str__(self):
        return f"Feedback: {self._date}, Text: {self.text}, Student: {self._student}, Tutor: {self._tutor}"