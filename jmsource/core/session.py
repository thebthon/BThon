import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

from ..Config import Config
from .bothseesion import bothseesion
from .client import JmthonClient
from .logger import logging

LOGS = logging.getLogger("سورس 𝗚𝗥")
__version__ = "2.10.6"

loop = None

if Config.STRING_SESSION:
    session = bothseesion(Config.STRING_SESSION, LOGS)
else:
    session = "jmthon"

try:
    jmsource = JmthonClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(
        f"STRING_SESSION WRONG PLZ MAKE A NEW SESSION - {e}\n كود سيشن تيليثون الذي وضعته غير صالح"
    )
    sys.exit()

try:
    if Config.STRING_SESSION2:
        jmsource2 = JmthonClient(
            bothseesion(Config.STRING_SESSION2, LOGS),
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            loop=loop,
            app_version=__version__,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
    else:
        jmsource2 = None
except Exception as e:
    print(f"STRING_SESSION2 - {str(e)}")
    sys.exit()


jmsource.tgbot = tgbot = JmthonClient(
    session="jmthonTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.TG_BOT_TOKEN)
