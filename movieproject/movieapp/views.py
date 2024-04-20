from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
from django.contrib import messages 

# Create your views here.
def index(request):
    mov=Movie.objects.all()
    m_name= {
        'movie_list': mov
    }
    return render(request,'index.html',m_name)

def details(request,id):
    m_deatils=Movie.objects.get(id=id)

    return render(request,'details.html',{'list1':m_deatils})


# add Data html page to databas

def add_movie(request):
    if request.method=="POST":
        a_name=request.POST.get('m_name')
        a_desc=request.POST.get('m_desc')
        a_year=request.POST.get('m_year')
        a_img=request.FILES['m_img']
        a_movie=Movie(name=a_name,decs=a_desc,year=a_year, img=a_img)
        a_movie.save()
    return render(request, 'add_movies.html')


#updating function

def update(request, id):
    #retrive data from Movie object from specified ID
    movie=Movie.objects.get(id=id)

    #create a movie from 
    form=MovieForm(request.POST or None, request.FILES, instance=movie)

    #check the from is valid or not
    if form.is_valid():
        #saving data

        form.save()

        #redirect to home page after saving
        return redirect ('/')
    
    #return the template with form and movie object
    return render(request, 'edit.html', {'forms':form,'movie':movie})

def delete_movie(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        messages.error(request, 'Movie not found')
        return redirect('/')

    if request.method == "POST":
        movie.delete()
        messages.success(request, 'Movie deleted successfully')
        return redirect('/')
    else:
        return render(request, 'delete_confirmation.html', {'movie': movie})