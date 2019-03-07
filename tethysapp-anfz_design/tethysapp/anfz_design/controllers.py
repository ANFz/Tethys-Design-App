from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    context = {}
    return render(request, 'anfz_design/home.html', context)


@login_required()
def proposal(request):
    context = {}
    return render(request, 'anfz_design/proposal.html', context)

@login_required()
def wireframe(request):
    context = {}
    return render(request, 'anfz_design/wireframe.html', context)

