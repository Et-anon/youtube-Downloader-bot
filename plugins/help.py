from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Just Send Any Youtube Url  (No playlist)  Also U Can use Search @vid 'vidNAME'"
    await message.reply_text(helptxt)
