from users import User, SupportUser

class TicketErrors(Exception):
    pass

class ValueTicketAuthorError(TicketErrors):
    pass

class ValueIdTicketError(TicketErrors):
    pass

class ValueProblemTextError(TicketErrors):
    pass

class ValueSupportUserError(TicketErrors):
    pass

class TicketNotAssignedError(TicketErrors):
    pass

class TicketAlreadyClosedError(TicketErrors):
    pass


class Ticket:
    def __init__(self, id_ticket, user, problem_text):
        self.ticket_author = user
        self.id_ticket =  id_ticket
        self.problem_text = problem_text
        self._status_ticket = "OPEN"
        self._support_user = None

    @property
    def ticket_author(self):
        return self._ticket_author

    @ticket_author.setter
    def ticket_author(self, value_user):
        if not isinstance(value_user, User):
            raise ValueTicketAuthorError('Ошибка с присвоением автора проблемы')
        self._ticket_author = value_user
    
    @property
    def problem_text(self):
        return self._problem_text
    
    @problem_text.setter
    def problem_text(self, value_text):
        if not isinstance(value_text, str):
            raise ValueProblemTextError('Ошибка в присвоении текста')
            
        if not value_text.strip():
            raise ValueProblemTextError('Текст проблемы не может быть пустым')
            
        self._problem_text = value_text

    @property
    def id_ticket(self):
        return self._id_ticket
    
    @id_ticket.setter
    def id_ticket(self, value_id):
        if not isinstance(value_id, int):
            raise ValueIdTicketError('Ошибка с присвоением ключа')
    
        if value_id <= 0:
            raise ValueIdTicketError('Ошибка с присвоением ключа')
            
        self._id_ticket = value_id

    @property
    def status_ticket(self):
        return self._status_ticket

    @property
    def support_user(self):
        return self._support_user

    def assign_support(self, support_user):
        if self._status_ticket == 'CLOSED':
            raise TicketAlreadyClosedError('Проблема уже закрыта')

        if not isinstance(support_user, SupportUser):
            raise ValueSupportUserError('Проблема с назначением сотрудника поддержки')

        self._support_user = support_user
        self._status_ticket = 'IN_PROGRESS'

    def close_ticket(self):
        if self._status_ticket == 'CLOSED':
            raise TicketAlreadyClosedError('Проблема уже закрыта')

        if self._support_user is None:
            raise TicketNotAssignedError('Невозможно закрыть проблему без назначенного сотрудника поддержки')

        self._status_ticket = 'CLOSED'
            

    def __str__(self):
        return (
            f'Автор проблемы - {self.ticket_author}\n'
            f'Текст проблемы - {self.problem_text}\n'
            f'Статус - {self.status_ticket}\n'
            f'Исполнитель - {self.support_user}'
        )