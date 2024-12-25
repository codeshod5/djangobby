from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from .models import Addroutes,Busform
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Addroutes)
@receiver(post_delete, sender=Addroutes)
def send_areas_update_to_websocket(sender, instance, **kwargs):
    
    channel_layer = get_channel_layer()

   
    updated_areas = list(Addroutes.objects.all().values('id', 'routenum', 'areas'))
    print("area is updated and signal is sentt")
    print(type(updated_areas))
    # print(updated_areas)
    

  
    async_to_sync(channel_layer.group_send)(
        'programmers',  # The group to send data to
        {
            'type': 'chat.message',
            'areas': updated_areas
        }
    )
    
@receiver(post_save,sender=Busform)
@receiver(post_delete,sender=Busform)
def send_map_update_to_websocket(sender,instance,**kwargs):
    channel_layer = get_channel_layer()

    updated_loc = list(Busform.objects.all().values('route_no','bus_no','number_plate','live_location_link'))
    print("this map is updated ")
    print(updated_loc)

    async_to_sync(channel_layer.group_send)(
        'updaters',
        {
            'type': 'mapup.message',
            'message':updated_loc
        }
    )


    