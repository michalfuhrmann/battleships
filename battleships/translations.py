ENGLISH_TRANSLATIONS = {
    "login": "Login",
    "logout": "Logout",
    "register": "Register",
    "index": "Index",
    "game_list": "Game List",
    "new_game": "New Game",
    "join_game": "Join Game",
    "app_user": "guest"
}

POLISH_TRANSLATIONS = {
    "login": "Zaloguj",
    "logout": "Wyloguj",
    "register": "Zarejestruj",
    "index": "Indeks",
    "game_list": "Lista gier",
    "new_game": "Nowa gra",
    "join_game": "Dolacz do gry",
    "app_user": "gosc"
}

LANGUAGES = {
    'EN': ENGLISH_TRANSLATIONS,
    'PL': POLISH_TRANSLATIONS
}

LANGUAGES_KEY = 'app_languages'


def get_translations(language):
    return LANGUAGES[language]


def get_available_languages():
    return {LANGUAGES_KEY:LANGUAGES.keys()}

