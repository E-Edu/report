from unittest import TestCase
from report.models.ticket import generate_uuid

class GenerateUUIDTest(TestCase):
    def test_generate_uuid(self):
        result = generate_uuid()
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 36)
        