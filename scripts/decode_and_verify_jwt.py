import requests
import base64
import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey


def decode_and_verify_jwt():
    with open("jwt.txt") as jwt_file:
        jwt_string = jwt_file.read()

    url = "http://localhost:8000/did"
    resp = requests.get(url)
    data = resp.json()

    encoded_public_key = data["verificationMethod"][0]["publicKeyJwk"]["x"]
    public_key = base64.b64decode(encoded_public_key)
    pem_formatted_public_key = Ed25519PublicKey.from_public_bytes(public_key).public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    payload = jwt.decode(jwt_string, pem_formatted_public_key, algorithms=["EdDSA"], verify=True)
    print(payload)


if __name__ == '__main__':
    decode_and_verify_jwt()
