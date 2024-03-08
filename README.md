# README

## Requirements:
* Python 3.10, or other compatible versions
* The following Python Packages:
  * base64
  * cryptography
  * django
  * json
  * jwt
  * requests

## Steps to run
1. Generating DID document and Ed25519 keys
``` sh
cd scripts
python generate_did_and_keys.py
```
2. Running Web server

``` shell
cd did_web_server
python manage.py 
```

3. Generate JWT
``` shell
cd scripts
python generate_jwt.py
```

4. Extract and verify payload
``` shell
cd scripts
python decode_and_verify_jwt.py
```
