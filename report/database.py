from report import db
from report import ma

class Ticket(db.Model):
    ticketId = db.Column(db.Integer, primary_key=True)
    taskId = db.Column(db.String(100))
    title = db.Column(db.String(200))
    body = db.Column(db.String(200))
    TicketType = db.Column(db.String(10))
    role = db.Column(db.String(3))
    user_id = db.Column(db.String(1000)) #! change when >1000 user

    def __init__(self, taskId, title, body, TicketType):
        self.taskId = taskId
        self.title = title
        self.body = body
        self.TicketType = TicketType


class TicketSchema(ma.Schema):
    class Meta:
        fields = ('ticketId', 'taskId', 'title', 'body', 'TicketType')


ticketSchema = TicketSchema()
ticketSchema_many = TicketSchema(many=True)
