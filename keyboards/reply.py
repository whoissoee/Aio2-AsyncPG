from utils import ReplyMarkupConstructor

class AdminMenuMarkup(ReplyMarkupConstructor):
    check_users = "📈 Посмотреть кол-во пользователей в бд"
    broadcast = "📣 Рассылка"
    get_users_file = "📩 Выгрузить пользователей в файл"

    def get(self):
        actions = [
            {"text": self.check_users},
            {"text": self.broadcast},
            {"text": self.get_users_file}
        ]
        schema = [2, 1]
        return self.markup(actions, schema, resize_keyboard=True)

class AdminCancelMarkup(ReplyMarkupConstructor):
    cancel_btn = "❌ Отменить"

    def get(self):
        return self.markup([{"text": self.cancel_btn}], [1], resize_keyboard=True)

class MainMenuMarkup(ReplyMarkupConstructor):
    start_btn = "👤 Профиль"
    settings_btn = "⚙️ Настройки"

    def get(self):
        actions = [
            {"text": self.start_btn},
            {"text": self.settings_btn}
        ]
        schema = [1, 1]
        return self.markup(actions, schema, resize_keyboard=True)

