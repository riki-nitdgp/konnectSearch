class BaseExceptions(Exception):

    def __init__(self, detail: str, status_code: int = 400):
        self._error = detail
        self._status_code = status_code

    @property
    def error(self):
        return self._error

    @property
    def status_code(self):
        return self._status_code


class InternalServiceException(BaseExceptions):
    pass


class ServiceException(BaseExceptions):
    pass


class JsonDecodeException(BaseExceptions):

    def __init__(self, error):
        self._error = error

    @property
    def error(self):
        return self._error
