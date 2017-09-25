class ApiException(Exception):
    def __init__(self, code ,message, errors):
        super(ApiException, self).__init__(message)
        self.errors = errors
        self.code = code

    def get_code(self):
        return self.code

    def errors(self):
        return self.errors