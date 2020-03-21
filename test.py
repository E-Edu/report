import jwt
asd = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')

jwt.decode(asd, 'secret123', algorithms=['HS256'])