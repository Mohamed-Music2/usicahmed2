from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BAAokFYkNkouh3MyD9WJzi6L-J5Kh_p1qRCj5KUluNf4Dvcl8YniPxTvqyCgeGKLQcAZSTxIC_ixRHwoDsls3IX4iDwR4y2OAhvdYJvFO6w4OyRunLg4R5hEH0AWzTFe_SLSdqNOIcB7YnbPebTljrCi4-YNm99oU9OGuqt_glN74Xz2J1EFWVXdx5rehErxH3WprgwhZjXWyqh-IiaZoWION15eSfScfhtTlsVOPaHh9lpPAriVDsd5i8Ktq3kyfjMpP1bJZAVbf1jG9H1j2RUV8YiTLaEITPxQvusecD5xPOOOa9VZAaq5YVjdZgo80khY5S5SbSsf94_QK3rJ9jNJAAAAAS2FcekA")
BOT_TOKEN = getenv("BOT_TOKEN","5409818512:AAHNVmbdbgAV_NBWmRl3cpU7Wpp2rWDzpz4")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph//file/36a15fa7b75b0f424bda6.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph//file/189fe27bff1207dd3eb85.jpg")
BOT_NAME = getenv("BOT_NAME", "TEAM EISA MUSIC")
API_ID = int(getenv("API_ID", "16050450"))
API_HASH = getenv("API_HASH", "0dd89e225b6ddd6f03e8135460d31177")
BOT_USERNAME = getenv("BOT_USERNAME", "lMl4ll_MUSIC_BOT") 
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "lMl4ll_MUSIC")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "BarEisa")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "D_o_m_A12") 
OWNER_NAME = getenv("OWNER_NAME", "lMl4ll")
ALIVE_NAME = getenv("ALIVE_NAME", "lMl4ll_MUSIC")
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://hussein87:Hussein87@cluster0.wynpz.mongodb.net/?retryWrites=true&w=majority")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5191100896").split()))
