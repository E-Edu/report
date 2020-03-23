from report import db
from report import ma


class Ticket(db.Model):
    ticketId = db.Column(db.Integer, primary_key=True)
    taskId = db.Column(db.String(100))
    title = db.Column(db.String(200))
    body = db.Column(db.String(200))
    TicketType = db.Column(db.String(10))
    role = db.Column(db.String(3))
    user_id = db.Column(db.String(1000))  # ! change when >1000 user
    isSloved = db.Column(db.Boolean(), default=False) 

    def __init__(self, taskId, title, body, TicketType, user_id):
        self.taskId = taskId
        self.title = title
        self.body = body
        self.TicketType = TicketType
        self.user_id = user_id

    def __repr__(self):
    	return f"<Ticket ({self.taskId}, {self.title}, {self.body}, {self.TicketType}, {self.user_id})>"


class TicketSchema(ma.Schema):
    class Meta:
        fields = ('ticketId', 'taskId', 'title', 'body', 'TicketType', 'isSloved')


ticketSchema = TicketSchema()
ticketSchema_many = TicketSchema(many=True)
db.create_all()

