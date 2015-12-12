import hashlib, uuid
from battleships.models import User

# key - hash, value - username
SESSIONS = {}


def create_session(username):
    salt = uuid.uuid4().hex
    string = username + salt
    string = string.encode('utf-8')
    user_session = hashlib.sha256(string).hexdigest()
    SESSIONS[user_session] = username
    return user_session


def get_logged_user(user_session):
    return SESSIONS.get(user_session)


def hash_password(password, salt=uuid.uuid4().hex):
    string = password + salt
    string = string.encode('utf-8')
    return salt, hashlib.sha256(string).hexdigest()


def user_login(username, password):
    user = User.objects.filter(username=username)
    if user:
        user = user[0]
        _, _password = hash_password(password, user.salt)
        if user.password == _password:
            return user
    return None


def user_register(username, password):
    if User.objects.filter(username=username):
        return False, 'uzytkownik istnieje'
    salt, hash = hash_password(password)
    User.objects.create(username=username, salt=salt, password=hash)
    return True, ''
