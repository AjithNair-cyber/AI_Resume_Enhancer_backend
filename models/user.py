from datetime import datetime, timezone

class User :
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
        self.created_at = datetime.now(timezone.utc)

    def getUser(self) :
        return {"email" : self.email, "password" : self.password, "name" : self.name, "created_at" : self.created_at}