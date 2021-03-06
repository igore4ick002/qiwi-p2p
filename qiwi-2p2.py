import asyncio
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class YourMod(loader.Module):
    """Description for module"""  # Translateable due to @loader.tds
    strings = {"cfg_doc": "This is what is said, you can edit me with the configurator",
               "name": "p2p Qiwi",
               "after_sleep": "We have finished sleeping!"}

    def __init__(self):
        self.config = loader.ModuleConfig("CONFIG_STRING", "hello", lambda m: self.strings("cfg_doc", m))

    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def oplatacmd(self, message):
        """Выставить щёт .oplata """
        logger.debug("We logged something!")
        await utils.answer(message, self.config["CONFIG_STRING"])
        await asyncio.sleep(5)  # Never use time.sleep
        await utils.answer(message, self.strings("after_sleep", message))
