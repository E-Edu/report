from tests.base_integration_test import BaseTest
from report.models.ticket import Ticket


class TicketTest(BaseTest):
    def test_db_ticket(self):
        with self.app_context():
            ticket = Ticket(
            task_id="1", 
            title="test title", 
            body="test body", 
            role=0, 
            report_reason="TROLLING", 
            user_id=1, 
            isSloved=False,
            response_title="test t",
            response_body="test b",
            support=True
            )
            self.assertEqual(Ticket.query.all(), [])
            ticket.save_to_db()
            self.assertIsNot(Ticket.query.all(), [])
            ticket.delete_from_db()
            self.assertEqual(Ticket.query.all(), [])

    def test_return_report(self):
        ticket = Ticket(
        ticket_id=1,
        task_id="1", 
        title="test title", 
        body="test body", 
        role=0, 
        report_reason="TROLLING", 
        user_id=1, 
        isSloved=False,
        response_title="test t",
        response_body="test b",
        support=True
        )
        data = ticket.return_report()
        self.assertDictEqual(data, {"ticket_id": 1, "task_id": "1", "user_id": 1, "title": "test title", "body": "test body", "report_reason": "TROLLING"})

    def test_return_support(self):
        ticket = Ticket(
        ticket_id=1,
        task_id="1", 
        title="test title", 
        body="test body", 
        role=0, 
        report_reason="TROLLING", 
        user_id=1, 
        isSloved=False,
        response_title="test t",
        response_body="test b",
        support=True
        )
        data = ticket.return_support()
        self.assertDictEqual(data, {"ticket_id": 1, "task_id": "1", "user_id": 1, "title": "test title", "body": "test body"})