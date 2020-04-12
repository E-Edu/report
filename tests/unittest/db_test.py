from tests.test_base import BaseTest
from report.database import Ticket

class DBTest(BaseTest):
    def test_create_ticket(self):
        ticket = Ticket(taskId=10, title="TestTicket1", body="Test Body 1", user_id=1)
        ticket2 = Ticket(taskId="10", title="TestTicket2", body="Test Body 2", user_id="2")

        #? ticket
        self.assertEqual(ticket.taskId, 10)
        self.assertEqual(ticket.title, "TestTicket1")
        self.assertEqual(ticket.body, "Test Body 1")
        self.assertEqual(ticket.user_id, 1)

        #? ticket2
        self.assertEqual(ticket2.taskId, 10)
        self.assertEqual(ticket2.title, "TestTicket2")
        self.assertEqual(ticket2.body, "Test Body 2")
        self.assertEqual(ticket2.user_id, 2)
