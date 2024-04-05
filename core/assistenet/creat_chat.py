from .model import OpenAI_Assistent

class Message_Gen:

    def __init__(self, assistent_kwargs):
        self.model = OpenAI_Assistent()
        self.assistent = self.model.create_assistent(**assistent_kwargs)
        
    def forming_message(
            self, 
            text:str, 
            user_id:str,
            thread=None):
        
        if thread != None:
            thread = self.model.create_thread()
        
        message = self.model.message_create(
                                thread=thread,
                                user_id=user_id,
                                message=text
                                )
        return thread
    
    def send_mess(self, thread):
        run = self.model.send_message(
                thread=thread,
                assistant=self.assistent
            )
        return self.model.get_response(thread=thread)[-1]
        
        

