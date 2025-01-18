import random
import secrets


class FakeData:

    @staticmethod
    def GetFakeEmail():
        return f"{secrets.token_hex(8)}@gmail.com"

    @staticmethod
    def GetRandomPassword():
        return secrets.token_urlsafe(random.randint(5, 15))