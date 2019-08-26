
class VectorZeroDivisionError(ZeroDivisionError):
    def __init__(self, *args, **kwargs):
        self.message = "Working with vectors will not allow you to divide by zero!"
        super().__init__(self.message, *args, **kwargs)
