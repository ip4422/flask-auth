from werkzeug.security import generate_password_hash, check_password_hash


user_list = []


class User:
    def __init__(self, public_id, username, email, password):
        self.public_id = public_id
        self.username = username
        self.email = email
        self.password = password

    @property
    def user_id(self):
        return self.public_id

    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2')
        return self.password

    def check_password(self, password):
        # not sure about this
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    def save(self):
        user_list.append(self)

    @staticmethod
    def get_by_email(email):
        email = email.lower().strip()
        user = next((user for user in user_list if user.email == email), None)
        return user

    @staticmethod
    def get_all():
        return user_list

    @staticmethod
    def get_by_id(user_id):
        user = next(
            (user for user in user_list if user.public_id == user_id), None)
        return user
