from unittest import TestCase
from report.response import *

class ResponseTest(TestCase):
    def test_return_response(self):
        res200 = response(200, Status.c_200, "/")
        res201 = response(201, Status.c_201, "/")
        res400 = response(400, Status.c_400, "/")
        res400c1 = response(400, Status.c_400, "/", Status.cm_1)
        res400c2 = response(400, Status.c_400, "/", Status.cm_2)
        res401 = response(401, Status.c_401, "/")
        res403 = response(403, Status.c_403, "/")
        res404 = response(404, Status.c_404, "/")
        res405 = response(405, Status.c_405, "/")
        res500 = response(500, Status.c_500, "/")
        res501 = response(501, Status.c_501, "/")

        self.assertIsNotNone(res200)
        self.assertIsNotNone(res201)
        self.assertIsNotNone(res400)
        self.assertIsNotNone(res400c1)
        self.assertIsNotNone(res400c2)
        self.assertIsNotNone(res401)
        self.assertIsNotNone(res403)
        self.assertIsNotNone(res404)
        self.assertIsNotNone(res405)
        self.assertIsNotNone(res500)
        self.assertIsNotNone(res501)