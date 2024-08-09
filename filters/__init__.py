from .is_admin import AdminFilter
from .is_premium import PremiumFilter

def setup_filters(dp) -> None:
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(PremiumFilter)
