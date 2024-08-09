from middlewares.is_user_saved import IsUserSavedMiddleware


def setup_middlewares(dp):
    dp.middleware.setup(IsUserSavedMiddleware())
