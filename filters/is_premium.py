# from typing import Union

# from aiogram.types import Message, CallbackQuery
# from aiogram.dispatcher.filters import BoundFilter

# from load_config import ADMINS
# from keyboards.inline import PayMenuMarkup


# class PremiumFilter(BoundFilter):
#     """ Filter to check is user pay premium. """
#     key = "is_premium"

#     def __init__(self, is_premium):
#         self.is_premium = is_premium

#     async def check(self, m: Union[Message, CallbackQuery]):
#         user_id = m.from_user.id
#         bot = m.bot
#         db = bot["db"]

#         if user_id in ADMINS:  # If user is admin - skip check.
#             return True

#         premium = await db.get_premium_for_user(user_id)

#         if premium == True:
#             return True

#         if type(m) == CallbackQuery:
#             await m.answer()
#             m = m.message

#         await m.answer(f"Чтобы пользоваться ботом приобретите подписку:",
#                        reply_markup=PayMenuMarkup().get())
#         return False

from typing import Union

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import BoundFilter

from load_config import ADMINS
from keyboards.inline import PayMenuMarkup


class PremiumFilter(BoundFilter):
    """ Filter to check if user has a premium subscription. """
    key = "is_premium"

    def __init__(self, is_premium):
        self.is_premium = is_premium

    async def check(self, m: Union[Message, CallbackQuery]):
        user_id = m.from_user.id
        bot = m.bot
        db = bot["db"]

        if user_id in ADMINS:  # If the user is an admin, skip the check.
            return True
        
        premium = await db.get_premium_for_user(user_id)

        if premium == True:
            return True

        if type(m) == CallbackQuery:
            await m.answer()
            m = m.message

        if premium == False:
            await m.answer(f"Чтобы пользоваться ботом, приобретите подписку:",
                           reply_markup=PayMenuMarkup().get())
        return False


# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
