
import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_reader import config
from handlers import fsm

# States System
# Intial state: `start`
# States: `select_course`, `manage_lectures`, `manage_notifications`
# Transitions: `start` -> `select_course` -> `start`
#              `start` -> `manage_lectures` -> `start`
#              `start` -> `manage_notifications` -> `start`
#              `start` -> `start`
# Handlers: `start` -> `select_course` -> `start`
#           `start` -> `manage_lectures` -> `start`
#           `start` -> `manage_notifications` -> `start`
#           `start` -> `start`


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher()
    bot = Bot(config.bot_token.get_secret_value())

    dp.include_router(fsm.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())