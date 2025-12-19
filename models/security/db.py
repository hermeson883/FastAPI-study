from models.security.user import User

class UserInDB(User):
    hashed_password: str