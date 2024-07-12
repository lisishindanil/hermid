from envparse import env
from tortoise import Tortoise

env.read_envfile('.env')

EXCHANGE_API = env.str('EXCHANGE_API')
COIN_API = env.str('COIN_API')

DB_USERNAME = env.str("DB_USERNAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_ADDRESS = env.str("DB_ADDRESS")
DB_PORT = env.int("DB_PORT")


# Setting up
async def setup_database() -> None:
    models = [
        "hermid.database.user",
    ]

    await Tortoise.init(
        db_url=f"asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_ADDRESS}:{DB_PORT}/hermid",
        modules={"models": models},
    )
    await Tortoise.generate_schemas()

    Tortoise.init_models(
        models,
        "models",
    )