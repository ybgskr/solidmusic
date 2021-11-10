from pyrogram import Client, filters, types
from base.bot_base import bot_client as bot
from base.player import player
from utils.functions.decorators import authorized_only


@Client.on_message(filters.command("pause"))
@authorized_only
async def pause(_, message: types.Message):
    chat_id = message.chat.id
    stats = await player.change_streaming_status("pause", chat_id)
    return await bot.send_message(
        message,
        stats,
        reply_message=True
    )


@Client.on_message(filters.command("resume"))
@authorized_only
async def resume_(_, message: types.Message):
    chat_id = message.chat.id
    stats = await player.change_streaming_status("resume", chat_id)
    return await bot.send_message(
        message,
        stats,
        reply_message=True
    )


@Client.on_message(filters.command("skip"))
@authorized_only
async def skip_(_, message: types.Message):
    chat_id = message.chat.id
    toxt, title = await player.change_stream(chat_id)
    return await bot.send_message(
        message,
        toxt,
        title,
        reply_message=True
    )


@Client.on_message(filters.command("vol"))
@authorized_only
async def change_vol_(_, message: types.Message):
    chat_id = message.chat.id
    vol = int(message.command[1])
    await player.change_vol(chat_id, vol)
    await bot.send_message(
        message,
        "vol_changed",
        str(vol),
        True
    )


@Client.on_message(filters.command("end"))
@authorized_only
async def end_stream_(_, message: types.Message):
    chat_id = message.chat.id
    await player.end_stream(chat_id)
    await bot.send_message(
        message,
        "track_ended",
        reply_message=True
    )
