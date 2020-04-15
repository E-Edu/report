from report import db
from datetime import datetime

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Text)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    ticket_type = db.Column(db.Text)
    role = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    isSloved = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit() 

    def __repr__(self):
	    return f"<Ticket (ticket_id {self.id}, task_id {self.task_id}, user_id {self.user_id}, role {self.role}, title {self.title})>"