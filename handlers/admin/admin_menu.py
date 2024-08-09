from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards.reply import AdminMenuMarkup, AdminCancelMarkup


async def send_menu(m: Message, state: FSMContext) -> None:
    await state.reset_state(with_data=True)
    await m.answer("Выберите действие:", reply_markup=AdminMenuMarkup().get())


def setup_admin_menu(dp) -> None:
    dp.register_message_handler(send_menu, text=["/admin", AdminCancelMarkup.cancel_btn], state='*', is_admin=True)

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
