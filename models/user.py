class User :
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def getUser(self) :
        return {"email" : self.email, "password" : self.password, "name" : self.name}