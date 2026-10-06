class TicketErrors(Exception):
    pass

class ValueIdTicketError(TicketErrors):
    pass

class ValueProblemTextError(TicketErrors):
    pass

class ValueTicketAuthorError(TicketErrors):
    pass

class Ticket:
    def __init__(self, id_ticket, user, problem_text):
        self.ticket_author = user
        self.id_ticket =  id_ticket
        self.problem_text = problem_text

    @property
    def ticket_author(self):
        return self._ticket_author

    @ticket_author.setter
    def ticket_author(self, value_user):
    
    
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

    def __str__(self):
        return (
            f'Автор проблемы - {self.ticket_author}\n'
            f'Текст проблемы - {self.problem_text}'
        )