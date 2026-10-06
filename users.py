class UsersErrors(Exception):
    pass

class ValueNameError(UsersErrors):
    pass

class ValueIdUserError(UsersErrors):
    pass


class User:
    def __init__(self, name, id_user):
        self.name = name
        self.id_user = id_user

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value_name):
        if not isinstance(value_name, str):
            raise ValueNameError('Ошибка в присвоении имени')
        
        if not value_name.strip():
            raise ValueNameError('Имя не может быть пустым')
        
        self._name = value_name
    
    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, value_id):
        if not isinstance(value_id, int):
            raise ValueIdUserError('Ошибка с присвоением ключа')

        if value_id <= 0:
            raise ValueIdUserError('Ошибка с присвоением ключа')
        
        self._id_user = value_id

    def __str__(self):
        return f'Пользователь - {self.name}'

class SupportUser(User):
    def __str__(self):
        return f'Пользователь поддержки - {self.name}'

