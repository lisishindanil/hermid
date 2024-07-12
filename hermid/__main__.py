from mubble import Token, API, Dispatch, Mubble

from hermid import dps
from .config import setup_database

api = API(Token.from_env(path_to_envfile=".env"))
dispatch = Dispatch()
for dp in dps:
    dispatch.load(dp)


bot = Mubble(api, dispatch=dispatch)
bot.loop_wrapper.add_task(setup_database())
bot.run_forever()
