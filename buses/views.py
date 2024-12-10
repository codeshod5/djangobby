from django.shortcuts import render
from django.http import HttpResponse
from .fillup import *
from .models import *
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import get_object_or_404



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


def remove(request,busid):
    data = get_object_or_404(Busform,id=busid)
    data.delete()
    return redirect('get_routes')

# def updatee(request,busid):
#     # form = Busroutes.objects.all()
#     if request.method == 'POST':
#         data = get_object_or_404(Busform,id=busid)
#         route_no = request.POST.get('route_no',data.route_no)
#         bus_no = request.POST.get('bus_no',data.bus_no)
#         live_location_link = request.POST.get('live_location_link',data.live_location_link)

#         route_no =route_no
#         bus_no = bus_no
#         live_location_link = live_location_link
#         data.save()
#         return redirect('get_routes')
#     return render(request,'update.html')

def updatee(request, busid):
    
    data = get_object_or_404(Busform, id=busid)

    if request.method == 'POST':
        
        route_no = request.POST.get('route_no', data.route_no)
        bus_no = request.POST.get('bus_no', data.bus_no)
        live_location_link = request.POST.get('live_location_link', data.live_location_link)

        
        data.route_no = route_no
        data.bus_no = bus_no
        data.live_location_link = live_location_link
        data.save()

        
        return redirect('get_routes')

    
    return render(request, 'update.html', {'data': data})


def addroutes(request):
    

    return render(request,'addroutes.html')

def get_areas(request):
   if request.method == 'POST':
        routenum = request.POST.get('routenum')
        areas = request.POST.get('areas')
        createe = Addroutes.objects.create(

            routenum = routenum,
            areas = areas
        )
        
        return redirect('get_areas')
   else:
       areass = Addroutes.objects.all()
       return render(request,'getarea.html',{'getting':areass})
       







# def updatee(request):
#     update_id = request.GET.get('update_id')
#     if update_id :
           
#            bus_entry=get_object_or_404(Busform,id=update_id)
#            form = Busroutes(request.POST or None, instance=bus_entry)
#            if request.method == 'POST' and form.is_valid():
#                form.save()
#                messages.success(request,"route update")
#                return redirect('get_routes')

# def updatee(request):
#     update_id = request.GET.get('update_id')  # Extract the update_id from the query string
#     bus_entry = get_object_or_404(Busform, id=update_id)
#     form = Busroutes(instance=bus_entry)  # Pre-fill form with the existing data

#     if request.method == 'POST':
#         form = Busroutes(request.POST, instance=bus_entry)
#         if form.is_valid():
#             form.save()  # Save the updated data
#             messages.success(request, "Route updated successfully!")
#             return redirect('get_routes')

#     return render(request, 'update.html', {'form': form, 'update_id': update_id})






            
















