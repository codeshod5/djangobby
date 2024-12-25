from django import forms

class Busroutes(forms.Form):
    route_no = forms.IntegerField(max_value=200)
    bus_no  = forms.IntegerField(max_value=100)
    number_plate = forms.CharField(max_length=5)
    live_location_link = forms.URLField(label='Google Maps Live Location Link')
    
   
