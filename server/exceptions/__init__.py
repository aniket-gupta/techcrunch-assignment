class BadRequest(Exception):

    def __init__(self, description):
        self.code = 400
        self.description = description
        super().__init__(description)


class NotFound(Exception):

    def __init__(self, description):
        self.code = 404
        self.description = description
        super().__init__(description)