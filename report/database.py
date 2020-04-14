from report import db
from datetime import datetime

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Text)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    ticket_type = db.Column(db.Text)
    ticket_id = db.Column(db.Text)
    role = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    isSloved = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, title, body, user_id, ticket_type, ticket_id, task_id):
        self.task_id = task_id
        self.title = title
        self.body = body
        self.user_id = user_id
        self.ticket_type = ticket_type
        self.ticket_id = ticket_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit() 

    def __repr__(self):
    	return f"<Ticket ({self.task_id}, {self.title}, {self.body}, {self.TicketType}, {self.user_id})>"