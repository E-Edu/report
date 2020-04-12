from report import db

class Ticket(db.Model):
    ticketId = db.Column(db.Integer, primary_key=True)
    taskId = db.Column(db.String(100)) #? Await GitHub answer
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    TicketType = db.Column(db.String(10)) #TODO ticket_type??
    role = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    isSloved = db.Column(db.Boolean(), default=False)

    def __init__(self, taskId, title, body, user_id):
        self.taskId = int(taskId)
        self.title = title
        self.body = body
        self.user_id = int(user_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
