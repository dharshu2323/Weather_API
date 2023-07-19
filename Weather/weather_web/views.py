from django.shortcuts import render,redirect
from .form import cityform
from .models import city
import requests
from django.contrib import messages
# Create your views here.
def home(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={},&appid=8de79fd02319e7babd69c7b64eb51458&units=metric'

    if request.method=="POST":
        form=cityform(request.POST)        
        if form.is_valid():
            NCity=form.cleaned_data['name']            
            CCity=city.objects.filter(name=NCity).count()
            if CCity==0:
                res=requests.get(url.format(NCity)).json()                
                if res['cod']==200:
                    form.save()
                    messages.success(request," "+NCity+" Added Successfully...!!!")
                else: 
                    messages.error(request,"City Does Not Exists...!!!")
            else:
                messages.error(request,"City Already Exists...!!!")      

    form=cityform()
    cities=city.objects.all()
    data=[]
    for city_instance in cities:        
        res=requests.get(url.format(city_instance.name)).json()   
        city_weather={
            'city':city_instance,
            'temperature' : res['main']['temp'],
            'description' : res['weather'][0]['description'],
            'country' : res['sys']['country'],
            'icon' : res['weather'][0]['icon'],
        }
        data.append(city_weather)  
    context={'data' : data,'form':form}
    return render(request,"weather.html",context)
    
def delete_city(request,CName):
    city.objects.get(name=CName).delete()
    messages.success(request," "+CName+" Removed Successfully...!!!")
    return redirect('Home')

      


    