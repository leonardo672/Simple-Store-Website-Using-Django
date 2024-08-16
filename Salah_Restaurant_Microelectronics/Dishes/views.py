from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Dishes

#def movie(requset, movie_id):
  # movie = Movie.objects.get(pk=movie_id)
  # if movie is not None:
  #    return render(requset, 'about.html', {'movie': movie})
  # else:
   #   raise Http404('Movie does not exist')
   

   
#def About(response):
 #  return render(response, "about.html")

#def F(response):
 #  return render(response, "1.html")

def HomeBase(response):
   return render(response, "HomeBase.html")

def home(response):
   # return HttpResponse('<h1>Home Page</h1>')
   Dish = Dishes.objects.all()
   return render(response, 'home.html', {'Dishes': Dish})

def ContactBase(response):
   return render(response, "ContactBase.html")

def AboutUsBase(response):
   return render(response, "AboutUsBase.html")

def BookingBase(response):
   return render(response, "BookingBase.html")

def MenuT(response):
   return render(response, "MenuT.html")

def AddToCartT(response):
   return render(response, "AddToCartT.html")