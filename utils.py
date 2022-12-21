import uuid

import sha3


def hasher(password: str) -> str:
    #hash data
    return sha3.sha3_224(password.encode("utf-8")).hexdigest()


def token_generator() -> str:
    #create token to user
    return str(uuid.uuid4()).replace("-", "")
