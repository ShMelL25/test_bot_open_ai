import os
import time
from openai import OpenAI

class OpenAI_Assistent:
    def __init__(self, api_key:str):

        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY", api_key),
        )

    def create_assistent(self, name=None, instructions=None, model=None):
        return self.client.beta.assistants.create(
                name="Леночка",
                instructions="Добрый  день, я представляю группу компаний БИТУМ ЭКСПРЕС В ВАШ ДОМ. Мы производим высоскокачественный битум. Скажите вам это интересно?",
                model="gpt-4"
            )
    
    def create_thread(self):
        return self.client.beta.threads.create()
    
    def message_create(self, thread, user_id:str, message:str):
        
        return self.client.beta.threads.messages.create(
                    thread_id=thread.id,
                    role=user_id,
                    content=message
                )
    
    def send_message(self, thread, assistant):
        run = self.client.beta.threads.runs.create(
                    thread_id=thread.id,
                    assistant_id=assistant.id,
                )
        return self.wait_on_run(
                    run=run,
                    thread=thread
                         ) 
    
    def wait_on_run(self, run, thread):
        while run.status == "queud" and run.status == "in_progress":
            run = self.client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            time.sleep(.5)
            
        return run
    
    def get_response(self, thread):
        return self.client.beta.threads.messages.list(thread_id=thread.id, order='asc')