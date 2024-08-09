from aiogram.utils.callback_data import CallbackData
from utils import InlineMarkupConstructor

class PayMenuMarkup(InlineMarkupConstructor):
    pay_cb = CallbackData("pay")

    def get(self):
        schema = [1]

        actions = [
            {"text": "Оформить подписку", "cb": self.pay_cb.new()},
        ]
        return self.markup(actions, schema)

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
