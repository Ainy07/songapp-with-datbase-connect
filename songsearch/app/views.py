from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from . models import *

# Create your views here.
def base(request):
    return render(request , 'base.html')

def signup(request):
    return render(request , 'signup.html')


def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
            return redirect("/signup/")
        elif User.objects.filter(phone=phone).exists():
            messages.error(request,"contact already exists")
            return redirect("/signup/")
        else:
            User.objects.create(name=name,email=email,password=password,phone=phone)
        return redirect("/login/")
    

def login(request):
    return render(request , 'login.html')


def login_form(request):
    if request.method =='POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if User.objects.filter(email=email).exists():
           obj = User.objects.get(email=email)
           password = obj.password
           if check_password(user_password, password):
                return redirect("/songs/")
           else:
            return HttpResponse('password incorrect')
        else:
            return HttpResponse("Email is not registered")
        
   
   
def songs(request):
    song = Song.objects.all()
    return render(request, 'song.html', {'song': song})


# def get_top_track(request):
#     sp = spotipy.Spotipy(auth="your-api-key")
#     results = sp.current_user_top_tracks(limit=10 , time_range='short_term')
#     tracks = []
#     for item in results['item']:
#         track ={
#             'name': item['name'],
#             'artist': item['artist'][0]['name'],
#             'album': item['album']['name']
            
#         }
#         tracks.append(track)
#         Track.objects.create(name=track['name'], artist=track['artist'],album=track['album'])
#     return JsonResponse({'tracks': tracks})    


# def track_list(request):
#     tracks = Track.objects.all()
#     return render(request, 'search.html' , {'tracks':tracks})

