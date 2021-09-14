# Import base modules
from loguru import logger
from yaml import safe_load

# Import aiogram
from aiogram import Bot, Dispatcher, executor

# Import bot
from HybridsRu_bot import setup_bot

if __name__ == "__main__":
    # Load bot config from file
    with open("config.yaml") as f:
        config = safe_load(f)
    logger.info(f"Loaded config from file: {config}")

    # Initialize bot
    bot = Bot(token=config["api_key"])
    bot["save_dir"] = config["save_dir"]
    dp = Dispatcher(bot)
    logger.info(f"Created bot with {config['api_key']} api_key")

    # Setup functions
    handlers_names = setup_bot(dp)
    logger.info(f"Created bot handlers: {handlers_names}")

    # Run bot
    logger.info("Let's go")
    executor.start_polling(dp)
