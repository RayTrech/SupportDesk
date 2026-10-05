class UsersErrors(Exception):
    pass

class ValueNameError(UsersErrors):
    pass

class ValueIdUserError(UsersErrors):
    pass


class User:
    def __init__(self, name, id_user):
        self.name = name
        self.id = id_user

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value_name):
        if not isinstance(value_name, str):
            raise ValueNameError('Ошибка в присвоении имени')
        self._name = value_name

        if value_name == ' ':
            return ValueNameError('Ошибка в присвоении имени')
    
    @property
    def id_user(self):
        return self._id_user

    @id.setter
    def id(self, value_id):
        if not isinstance(value_id, int):
            raise ValueIdUserError('Ошибка с присвоением ключа')
        self._id_user = value_id

        if value_id <= 0:
            raise ValueIdUserError('Ошибка с присвоением ключа')
        self._id_user = value_id
        

    def __str__(self):
        return f'Пользователь - {self.name}'

class SupportUser(User):
    def __str__(self):
        return f'Пользователь поддержки - {self.name}'

user1 = User("Alex", 1)
user2 = SupportUser("Bob", 2)

print(user1)