from src import personas
from asgiref.sync import sync_to_async

async def official_handle_response(message, client) -> str:
    return await sync_to_async(client.chatbot.ask)(message)

# resets conversation and asks chatGPT the prompt for a persona
async def switch_persona(persona, client) -> None:
    if client.chat_model ==  "UNOFFICIAL":
        client.chatbot.reset_chat()
        async for _ in client.chatbot.ask(personas.PERSONAS.get(persona)):
            pass
    elif client.chat_model == "OFFICIAL":
        client.chatbot = client.get_chatbot_model(prompt=personas.PERSONAS.get(persona))
