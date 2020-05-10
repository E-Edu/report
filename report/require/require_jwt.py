from report.config import VenVar
import jwt
def require_jwt(auth_header):
    try:
        userdata = jwt.decode(auth_header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        return userdata
    except:
        return False