# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer, SyncConsumer
from asgiref.sync import async_to_sync
from channels.exceptions import StopConsumer
class AreasUpdateConsumer(SyncConsumer):
    def websocket_connect(self,event):
        # print("web connect..",event)
        # print("channel layer ",self.channel_layer)
        # print("channel_name",self.channel_name)

        async_to_sync(self.channel_layer.group_add)(
            'programmers',
            self.channel_name
        )
        self.send({
            'type':'websocket.accept'
        })

       

        # print()
   
    
    def websocket_receive(self,event):
        # print("message had rcived",event)
        async_to_sync(self.channel_layer.group_send)(
            'programmers',
            {
                'type':'chat.message',
                'message':event
            }

        )
    
    
    def chat_message(self, event):
        # This method handles the 'chat.message' type events
        # print('Event received in chat_message:', event)
        event_as_string = json.dumps(event)
        self.send({
            'type':'websocket.send',
            'text':event_as_string
        })
        # print("this is event ares",event['areas'])
        # print("this is type of event ",type(event['areas']))
        # self.send({
        #     'type': 'websocket.send',
        #     'text': event,  # Broadcast the message back to WebSocket
        # })

    
    def websocket_disconnect(self,event):
        print("websocket sdiscoont",event)
        print("channel layer..",self.channel_layer)
        print("channel name...",self.channel_name)

        async_to_sync(self.channel_layer_discard)(
            'programmers',
            self.channel_name
        )
        raise StopConsumer()
 
class MapUpdate(SyncConsumer):
    def websocket_connect(self,event):
        print("web connect..",event)
        print("channe_layer",self.channel_layer)
        print("channel_name",self.channel_name)

        async_to_sync(self.channel_layer.group_add)(
            'updaters',
            self.channel_name
        )
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        print("message recive2 ..",event)
        async_to_sync(self.channel_layer.group_send)(
            'updaters',
            {
                'type':'mapup.message',
                'message':event
            }
        )
    def mapup_message(self,event):
        print('event recived in updatempa..',event)
        event_as_str = json.dumps(event)
        self.send({
            'type': 'websocket.send',
            'text':event_as_str
        })


    def websocket_disconnect(self,event):
        print("web disconnect..",event)



        

        
   



        
 