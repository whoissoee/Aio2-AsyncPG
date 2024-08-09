from .admin import setup_admin
from .private import setup_private


def setup_handlers(dp) -> None:
    setup_admin(dp)
    setup_private(dp)
