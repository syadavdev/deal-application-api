import base64
import jwt
import hmac
import hashlib

# Return base 64 encode string of a string passed
def base64Encoded(str):
	encoded = base64.b64encode(bytes(str,"utf-8"))
	return encoded.decode("utf-8")

# Return JSON Web Token encoded string contains headers + payload and secret
def jwtHS256Encode(payload, secret):
	encoded = jwt.encode(payload , secret, algorithm='HS256')
	return encoded.decode("UTF-8")

def encodeByHMACSHA256(payload, secret):
	encoded = hmac.new(secret.encode("UTF-8"), payload.encode("UTF-8"), hashlib.sha256).hexdigest()
	return encoded

#Return payload info out of encoded token string
def jwtHS256Decode(encoded,secret):
	return jwt.decode(encoded,secret,algorithms=['HS256'])
