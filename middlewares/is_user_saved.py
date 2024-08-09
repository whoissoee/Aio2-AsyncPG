from aiogram.types import InlineQuery, Message
from aiogram.dispatcher.middlewares import BaseMiddleware


class IsUserSavedMiddleware(BaseMiddleware):
    """ Checks is user saved to the database and adds if no. """

    async def on_pre_process_message(self, message: Message, data):
        user_id = message.from_user.id
        username = message.from_user.username
        db = message.bot["db"]

        if not await db.get_user_by_id(user_id):
            await db.add_user(user_id, username)
 
