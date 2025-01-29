import requests


class RequestsApi:
    def __init__(self, base_url):
        self.session = requests.session()
        self.base_url = base_url

    def Get(self, endpoint):
        response = self.session.get(f"{self.base_url}/{endpoint}")
        return response

    def Post(self, endpoint, payload):
        response = self.session.post(f"{self.base_url}/{endpoint}", json = payload)
        return response

    def Put(self, endpoint, payload):
        response = self.session.put(f"{self.base_url}/{endpoint}", json = payload)
        return response

    def Delete(self, endpoint):
        response = self.session.delete(f"{self.base_url}/{endpoint}")
        return response

    def Close_Session(self):
        self.session.close()
