from django.shortcuts import render
from django.http import HttpResponse
from .fillup import *
from .models import *
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib import messages



def fillroute(request):
   
    form = Busroutes()  # Empty form for GET request
    routess = Busform.objects.all()
    
    # Render the form for both GET and invalid POST requests
    return render(request, 'foms.html', {'form': form,'routess':routess})

        
def get_routes(request):
    if request.method == 'POST':
        form = Busroutes(request.POST)
        

        if form.is_valid():
            route_no = form.cleaned_data['route_no']
            if Busform.objects.filter(route_no=route_no).exists():
                messages.error(request, "Route number already exists. Please update or delete.")
                return redirect('fillroute')


            

            # Create a new Busform entry
            Busform.objects.create(
                route_no=form.cleaned_data['route_no'],
                bus_no=form.cleaned_data['bus_no'],
                number_plate=form.cleaned_data['number_plate'],
                live_location_link=form.cleaned_data['live_location_link']
            )


            
            return redirect('get_routes')
    else:
        form = Busroutes()

    
    
    query = request.GET.get('search', "")
    if query:
        # Filter Busform entries based on the search query
        busform = Busform.objects.filter(
            Q(route_no__icontains=query) | 
            Q(bus_no__icontains=query) | 
            Q(number_plate__icontains=query)
        )
    else:
        # If no search query, show all entries
        busform = Busform.objects.all()

    return render(request, 'location.html', {'form': form, 'busform': busform, 'search_query': query})


def remove(request):
















