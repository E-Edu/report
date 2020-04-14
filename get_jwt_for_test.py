import jwt
import os

output = jwt.encode({"user_id": 14, "role": 0}, os.getenv("JWT_SECRET"), algorithm="HS512")

print(output)