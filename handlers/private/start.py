from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import ChatTypeFilter

from keyboards.reply import MainMenuMarkup

async def start_msg(m: Message) -> None:
    reply_markup = MainMenuMarkup().get()
    
    await m.answer(f'Приветствую тебя в боте!', reply_markup=reply_markup)



def setup_start(dp) -> None:
    dp.register_message_handler(lambda m: start_msg(m), ChatTypeFilter(ChatType.PRIVATE), is_premium=True, commands=["start"])


# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
