import re
from mubble import CallbackQuery, Dispatch, ABCMiddleware, Message
from mubble.bot.dispatch.context import Context

from hermid.database import User


dp = Dispatch()

@dp.message.register_middleware()
class ContextMessage(ABCMiddleware[Message]):
    async def pre(self, event: Message, ctx: Context) -> bool:
        user = await User.get_or_none(uid=event.from_user.id)
        if user is None:
            user = await User.create(
                uid = event.from_user.id,
                name = event.from_user.first_name
            )
        ctx.set("user", user)

        return True


@dp.callback_query.register_middleware()
class ContextCallback(ABCMiddleware[CallbackQuery]):
    async def pre(self, event: CallbackQuery, ctx: Context) -> bool:
        user = await User.get_or_none(uid=event.from_user.id)
        if user:
            ctx.set("user", user)
        return True