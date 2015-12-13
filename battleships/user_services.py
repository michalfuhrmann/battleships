import hashlib
import uuid

from battleships.models import User


# key - hash, value - username
SESSION_COOKIE = 'session-cookie'
LANGUAGE_COOKIE = 'language-cookie'
DEFAULT_LANGUAGE = "EN"
SESSIONS = {}


def create_session(username):
    salt = uuid.uuid4().hex
    string = username + salt
    string = string.encode('utf-8')
    user_session = hashlib.sha256(string).hexdigest()
    SESSIONS[user_session] = username
    return user_session


def add_language_cookie(response, language):
    response.set_cookie(LANGUAGE_COOKIE, language)


def get_language_cookie(request):
    language_from_cookie = request.COOKIES.get(LANGUAGE_COOKIE)
    if language_from_cookie is None:
        return DEFAULT_LANGUAGE
    return language_from_cookie


def get_user_session(request):
    return request.COOKIES.get(SESSION_COOKIE)


def get_current_username_by_user_session(user_session):
    return SESSIONS.get(user_session)


def get_current_username_by_request(request):
    return get_current_username_by_user_session(get_user_session(request))


def get_current_user(request):
    username = get_current_username_by_request(request)
    return User.objects.get(username=username)


def add_user_cookie(response, user_session):
    response.set_cookie(SESSION_COOKIE, user_session)


def invalidate_session(user_session):
    if user_session in SESSIONS:
        del SESSIONS[user_session]


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
