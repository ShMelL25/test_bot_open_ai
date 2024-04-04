import os
import time
from openai import OpenAI

class OpenAI_Assistent:
    def __init__(self, api_key:str):

        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY", api_key),
        )

    def create_assistent(self):
        return self.client.beta.assistants.create(
                name="Леночка",
                instructions="Добрый  день, я представляю группу компаний БИТУМ ЭКСПРЕС В ВАШ ДОМ. Мы производим высоскокачественный битум. Скажите вам это интересно?",
                model="gpt-4"
            )
    
    def create_thread(self):
        return self.client.beta.threads.create()
    
    def message_create(self, thread, user_id:str, message:str):
        pass
    
    def send_message(self, thread, assistant):
        run = self.client.beta.threads.runs.create(
                    thread_id=thread.id,
                    assistant_id=assistant.id,
                )
        return run
