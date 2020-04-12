import jwt

output = jwt.encode({"user_id": 14, "role": 0}, "save", algorithm="HS512")

print(output)