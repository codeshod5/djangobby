from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket concett...',event)
        print("channel layer",self.channel_layer)
        print("channel name",self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            'transpores',
            self.channel_name
        )
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print('message recevied', event['text'])

        # self.send(text_data="Acknowledged: " ,event)
    
    def websocket_disconnect(self,event):
        print('websocket disconnected.....',event)
        print('websocket concett...',event)
        print("channel layer",self.channel_layer)
        print("channel name",self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            'transpores',
            self.channel_name
        )
        raise StopConsumer()
    



    
# class MyAsyncConsumer(AsyncConsumer):
#     async def websocket_connect(self,event):
#         print('websocket concett...',event)
    
#     async def websocket_receive(self,event):
#         print('message recevied',event)
    
#     async def websocket_disconnect(self,event):
#         print('websocket disconnected.....',event)

    
