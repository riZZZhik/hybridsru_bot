from loguru import logger
from yaml import safe_load

if __name__ == "__main__":
    # Download bot config from file
    with open("config.yaml") as f:
        config = safe_load(f)

    logger.info(f"Loaded config from file: {config}")

