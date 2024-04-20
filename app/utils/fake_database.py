import hashlib

hash_obj = hashlib.sha256()
byte_pass = "111".encode()
hash_obj.update(byte_pass)
hex_pass = hash_obj.hexdigest()

fake_users_db = {
    "aaa": {
        "username": "aaa",
        "hashed_password": hex_pass,
        "id": 1
    }
}

cards = {
    "1": {
        "number": "1111 1111 1111 1111",
        "name": "John Doe",
        "date": "10/25",
        "cvc": "123",
    }
}