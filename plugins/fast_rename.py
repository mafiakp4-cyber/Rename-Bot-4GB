from pyrogram import Client, filters

@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def fast_rename(client, message):
    file = message.document or message.video or message.audio
    
    # User से नया नाम ले लो (simple example में fixed name रखा है)
    new_name = "Renamed_" + file.file_name
    
    await message.reply_document(
        file.file_id,
        file_name=new_name,
        caption=f"✅ Instantly Renamed to **{new_name}**"
    )
