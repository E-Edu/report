from unittest import TestCase
from report.models.ticket import Ticket

class TestTicket(TestCase):
    def test_create_ticket(self):
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

        self.assertEqual(ticket.task_id, "1")
        self.assertEqual(ticket.title, "test title")
        self.assertEqual(ticket.body, "test body")
        self.assertEqual(ticket.role, 0)
        self.assertEqual(ticket.report_reason, "TROLLING")
        self.assertEqual(ticket.user_id, 1)
        self.assertEqual(ticket.isSloved, False)
        self.assertEqual(ticket.response_title, "test t")
        self.assertEqual(ticket.response_body, "test b")
        self.assertEqual(ticket.support, True)
