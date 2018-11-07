from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
from .models import Album, Description


def homepage(request):

    album1 = Album.objects.get(id=1)
    album2 = Album.objects.get(id=2)
    album3 = Album.objects.get(id=3)
    album4 = Album.objects.get(id=4)

    description1 = Description.objects.get(id=1)
    description2 = Description.objects.get(id=3)
    description3 = Description.objects.get(id=4)
    description4 = Description.objects.get(id=5)

    context = {
        "album1": album1, "album2": album2, "album3": album3,
        "album4": album4, "description1": description1, "description2": description2,
        "description3": description3, "description4": description4
    }
    return render(request, 'home/homePage.html', context)


def startup(request):
    album1 = Album.objects.get(id=1)
    album2 = Album.objects.get(id=2)
    album3 = Album.objects.get(id=3)
    album4 = Album.objects.get(id=4)

    description1 = Description.objects.get(id=1)
    description2 = Description.objects.get(id=3)
    description3 = Description.objects.get(id=4)
    description4 = Description.objects.get(id=5)

    context = {
        "album1": album1, "album2": album2, "album3": album3,
        "album4": album4, "description1": description1, "description2": description2,
        "description3": description3, "description4": description4
    }
    return render(request, 'home/startUpPage.html', context)


def album_red(request):
    album1 = Album.objects.get(id=1)
    album2 = Album.objects.get(id=2)
    album3 = Album.objects.get(id=3)
    album4 = Album.objects.get(id=4)

    description1 = Description.objects.get(id=1)
    description2 = Description.objects.get(id=3)
    description3 = Description.objects.get(id=4)
    description4 = Description.objects.get(id=5)

    context = {
        "album1": album1, "album2": album2, "album3": album3,
        "album4": album4, "description1": description1, "description2": description2,
        "description3": description3, "description4": description4
    }
    return render(request, 'home/albumRed.html', context)


def album_roads(request):
    album1 = Album.objects.get(id=1)
    album2 = Album.objects.get(id=2)
    album3 = Album.objects.get(id=3)
    album4 = Album.objects.get(id=4)

    description1 = Description.objects.get(id=1)
    description2 = Description.objects.get(id=3)
    description3 = Description.objects.get(id=4)
    description4 = Description.objects.get(id=5)

    context = {
        "album1": album1, "album2": album2, "album3": album3,
        "album4": album4, "description1": description1, "description2": description2,
        "description3": description3, "description4": description4
    }
    return render(request, 'home/albumRoads.html', context)


def album_world(request):
    album1 = Album.objects.get(id=1)
    album2 = Album.objects.get(id=2)
    album3 = Album.objects.get(id=3)
    album4 = Album.objects.get(id=4)

    description1 = Description.objects.get(id=1)
    description2 = Description.objects.get(id=3)
    description3 = Description.objects.get(id=4)
    description4 = Description.objects.get(id=5)

    context = {
        "album1": album1, "album2": album2, "album3": album3,
        "album4": album4, "description1": description1, "description2": description2,
        "description3": description3, "description4": description4
    }
    return render(request, 'home/albumWorld.html', context)


def album_california(request):
    album1 = Album.objects.get(id=1)
    album2 = Album.objects.get(id=2)
    album3 = Album.objects.get(id=3)
    album4 = Album.objects.get(id=4)

    description1 = Description.objects.get(id=1)
    description2 = Description.objects.get(id=3)
    description3 = Description.objects.get(id=4)
    description4 = Description.objects.get(id=5)

    context = {
        "album1": album1, "album2": album2, "album3": album3,
        "album4": album4, "description1": description1, "description2": description2,
        "description3": description3, "description4": description4
    }
    return render(request, 'home/albumCalifornia.html', context)







