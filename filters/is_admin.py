from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter

from load_config import ADMINS


class AdminFilter(BoundFilter):
    """ Filter to check whether the user is an admin. """
    key = "is_admin"

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, m: Message):
        return m.from_user.id in ADMINS

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
