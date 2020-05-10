from flask_restful import reqparse

class CreateTicketParser():
    def parser_args():
        parser = reqparse.RequestParser()
        parser.add_argument("task_id", type=str, help="task_id can not be blank")
        parser.add_argument("title", type=str, help="title can not be blank")
        parser.add_argument("body", type=str, help="body can not be blank")
        parser.add_argument("report_reason", type=str, help="report_reason can not be blank")
        data = parser.parse_args()
        return data

class EditTicketParser():
    def parser_args():
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, help="title can not be blank")
        parser.add_argument("body", type=str, help="body can not be blank")
        data = parser.parse_args()
        return data

class SolveTicketParser():
    def parser_args():
        parser = reqparse.RequestParser()
        parser.add_argument("is_troll", type=bool, help="is_troll can not be blank")
        data = parser.parse_args()
        return data