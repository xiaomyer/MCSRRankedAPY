class DataNotFoundException(Exception):
  def __init__(self, path: str, params: dict):
    self.path = path
    self.params = params

  def __str__(self):
    return f"Path {self.path} with params {self.params}"


class WrongParametersException(Exception):
  def __init__(self, path: str, params: dict, message: str):
    self.path = path
    self.params = params
    self.message = message

  def __str__(self):
    return f"Path {self.path} with params {self.params}: {self.message}"


class TooManyRequestsException(Exception):
  def __init__(self, path: str, params: dict, message: str):
    self.path = path
    self.params = params
    self.message = message

  def __str__(self):
    return f"Path {self.path} with params {self.params}: {self.message}"
