from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {

    }

    return render(request, 'mysnowpackapp/home.html', context)

def mapview(request):
    context = {

    }

    return render(request, 'mysnowpackapp/mapview.html', context)


def dataservices(request):
    context = {

    }

    return render(request, 'mysnowpackapp/dataservices.html', context)


def about(request):
    context = {

    }

    return render(request, 'mysnowpackapp/about.html', context)

def proposal(request):
    context = {

    }

    return render(request, 'mysnowpackapp/proposal.html', context)

def mockups(request):
    context = {

    }

    return render(request, 'mysnowpackapp/mockups.html', context)