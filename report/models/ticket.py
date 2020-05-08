from sqlalchemy.dialects.postgresql import UUID
from report import db
from datetime import datetime
import uuid, json

def generate_uuid():
    return str(uuid.uuid4())

class Ticket(db.Model):
    ticket_id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    task_id = db.Column(db.String(40))
    user_id = db.Column(db.String(40))
    role = db.Column(db.Integer)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    response_title = db.Column(db.Text)
    response_body = db.Column(db.Text)
    support = db.Column(db.Boolean, default=False)
    report_reason = db.Column(db.Text)
    isSloved = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def return_report(self):
        return {"ticket_id": self.ticket_id, "task_id": self.task_id, "user_id": self.user_id, "title": self.title, "body": self.body, "report_reason": self.report_reason}

    def return_support(self):
        return {"ticket_id": self.ticket_id, "task_id": self.task_id, "user_id": self.user_id, "title": self.title, "body": self.body}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()