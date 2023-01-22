from aiogram.dispatcher.filters.state import State, StatesGroup


class ShopState(StatesGroup):
    category = State()
    products = State()
    nums = State()
    cart = State()
    main = State()
    end = State()
    check = State()
