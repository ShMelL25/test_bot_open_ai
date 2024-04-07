from .model import OpenAI_Assistent

class Message_Gen:

    def __init__(self):
        self.model = OpenAI_Assistent()

    def _assistent_(self, 
                 assistent_kwargs, 
                 assistent_api:str=None):
        
        if assistent_api==None:
            self.assistent = self.model.create_assistent(**assistent_kwargs)
            self.assistent_id = self.assistent.id
        return self.assistent

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
        return thread, message
    
    def send_mess(self, thread_id):
        run = self.model.send_message(
                thread_id=thread_id,
                assistant=self.assistent_id
            )
        return self.model.get_response(thread_id=thread_id)[-1]
    
    def check_user(self):
        pass
        
        

