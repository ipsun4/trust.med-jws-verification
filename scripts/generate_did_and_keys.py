import base64
import json

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization


def generate_did_and_keys():

    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    keypair_json = {
        "public_key": base64.b64encode(
            public_key.public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw
        )).decode("utf-8"),
        "private_key": base64.b64encode(
            private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption()
        )).decode("utf-8")
    }
    with open("keys.json", "w") as f:
        json.dump(keypair_json, f, indent=2)

    did_document = {
        "@context": [
            "https://www.w3.org/ns/did/v1",
            "https://w3id.org/security/suites/jws-2020/v1"
        ],
        "id": "did:web:example.com",
        "verificationMethod": [
            {
                "id": "did:web:example.com#key-0",
                "type": "JsonWebKey2020",
                "controller": "did:web:example.com",
                "publicKeyJwk": {
                    "kty": "OKP",
                    "alg": "EdDSA",
                    "crv": "Ed25519",
                    "x": base64.b64encode(public_key.public_bytes_raw()).decode("utf-8")
                }
            }
        ],
        "authentication": [
            "did:web:example.com#key-0",
        ],
        "assertionMethod": [
            "did:web:example.com#key-0",
        ],
        "keyAgreement": [
            "did:web:example.com#key-0"
        ]
    }
    with open("did.json", "w") as outfile:
        json.dump(did_document, outfile, indent=2)


if __name__ == "__main__":
    generate_did_and_keys()
