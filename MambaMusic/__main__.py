import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from MambaMusic import LOGGER, app, userbot
from MambaMusic.core.call import Anony
from MambaMusic.misc import sudo
from MambaMusic.plugins import ALL_MODULES
from MambaMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("MambaMusic.plugins" + all_module)
    LOGGER("MambaMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://files.catbox.moe/wcjiil.jpg")
    except NoActiveGroupCall:
        LOGGER("MambaMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("MambaMusic").info(
        "\x4d\x61\x6d\x62\x61\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x73\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\x20\x0a\x44\x6f\x6e\x27\x74\x20\x66\x6f\x72\x67\x65\x74\x20\x74\x6f\x20\x76\x69\x73\x69\x74\x20\x40\x4f\x46\x46\x49\x43\x49\x41\x4c\x5f\x4d\x41\x4d\x42\x41\x5f\x4e\x45\x54\x57\x4f\x52\x4b
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("MambaMusic").info("Stopping Mamba Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
