class UseNotFoundException(BaseException):
    description = 'User does not exists'


class WrongPasswordException(BaseException):
    description = 'invalid password'


class UserAlreadyExist(BaseException):
    description = 'user with such login already exist'
