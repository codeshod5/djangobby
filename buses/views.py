from django.shortcuts import render
from django.http import HttpResponse
from .fillup import *
from .models import *
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Count
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import requests


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
            routenum=routenum,
            areas=areas
        )
        return redirect('get_areas')
    else:
        areass = Addroutes.objects.all()
        query = request.GET.get('search', "")

        if query:
            filtered_areas = Addroutes.objects.filter(
                Q(routenum__icontains=query) |
                Q(areas__icontains=query)
            )
        else:
            filtered_areas = Addroutes.objects.all()

        return render(request, 'getarea.html', {'getting': areass, 'filtered_areas': filtered_areas})

   
def areas_update(request,areaid):
    data = get_object_or_404(Addroutes,id=areaid)

    if request.method=='POST':
        routenum = request.POST.get('routenum',data.routenum)
        areas = request.POST.get('areas',data.areas)

        data.routenum = routenum
        data.areas = areas
        data.save()
        return redirect('home_areas')
    return render(request,'reupdatearea.html',{'data':data})


def usercred(request):
    if request.method=='POST':
        email  = request.POST.get('email')
        timee = request.POST.get('time')
        userarea = request.POST.get('userarea')

        createe = Userlocred.objects.create(
            email = email,
            userarea = userarea,
            usertiming = timee


        )

        return HttpResponse(request,"the data is saved")




    

    return render(request,'usercred.html')

def plot_areas(request):
    values = Userlocred.objects.filter(usertiming="08:45").values('userarea').annotate(area_count=Count('id'))
    data_dict = {item['userarea']:item['area_count'] for item in values}
    areas = data_dict.keys()
    counts = data_dict.values()

    fig,ax = plt.subplots()
    ax.barh(areas,counts,color='skyblue')

    ax.set_xlabel('count of users')
    ax.set_ylabel('areas')
    ax.set_title('user count by area')
    # ax.set_xlim(1, 20)

    buffer = BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(buffer)

    return HttpResponse(buffer.getvalue(),content_type='image/png')

def api_areas(request):


    return render(request,'apiareas.html')

   
    



def display_chart(request):
    
    return render(request,'chart.html')

def home_page(request):
    return render(request,'homepage.html')

def home_areas(request):
    query = request.GET.get('search',"")
    if query:
        filtered_areas = Addroutes.objects.filter(
            Q(routenum__icontains=query)|
            Q(areas__icontains=query)
        )
    else:
        filtered_areas = Addroutes.objects.all()


    return render(request,'homeareas.html',{'filtered_areas':filtered_areas})

def register_page(request):

    return render(request, 'usercred.html')
    



def chatt(request):
    return render(request,'chatt.html')
   
       







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






            
















