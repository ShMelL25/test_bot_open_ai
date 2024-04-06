from .model import OpenAI_Assistent

class Message_Gen:

    def __init__(self, assistent_kwargs):
        self.model = OpenAI_Assistent()
        self.assistent = self.model.create_assistent(**assistent_kwargs)
        
    def forming_message(
            self, 
            text:str, 
            user_id:str,
            thread_id=None):
        
        if thread_id != None:
            thread = self.model.create_thread()
            thread_id = thread.id
        
        message = self.model.message_create(
                                thread_id=thread_id,
                                user_id=user_id,
                                message=text
                                )
        return thread
    
    def send_mess(self, thread_id):
        run = self.model.send_message(
                thread_id=thread_id,
                assistant=self.assistent
            )
        return self.model.get_response(thread_id=thread_id)[-1]
    
    def check_user(self):
        pass
        
        

