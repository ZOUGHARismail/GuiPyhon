from user import User
class Admin(User):
    def __init__(self, login, pwd):
        super().__init__(login, pwd)


    def afficher(self):
        from form_admin import FormAdmin
        FormAdmin()
        
