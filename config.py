import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "23009724"))
API_HASH = os.environ.get("API_HASH", "66a87d259426e268bdd765fb4c635f2b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7824911074:AAEk7FKLig0x48wL3Evzw7-pAxJ5Gx6_lh4")
ADMIN = int(os.environ.get("ADMIN", "7405406082"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "kannadarockersdg")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002334874259"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://hello:Preethu@cluster0.isgp5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "madflixbotz")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://envs.sh/aBy.jpg")


# SHORTNER_URL = os.environ.get("SHORTNER_URL", "")
# SHORTNER_API = os.environ.get("SHORTNER_API", "")
# TOKEN_TIMEOUT = os.environ.get("TOKEN_TIMEOUT", "")
