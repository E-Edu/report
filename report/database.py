from report import db
from report import ma

class Ticket(db.Model):
    ticketId = db.Column(db.Integer, primary_key=True)
    taskId = db.Column(db.Integer)
    title = db.Column(db.String)
    body = db.Column(db.String)
    TicketType = db.Column(db.String)

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

db.create_all()

