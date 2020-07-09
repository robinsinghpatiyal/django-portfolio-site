from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Projects

# Create your views here.
def allprojects(request):
    projects = Projects.objects
    return render(request, 'projects/allprojects.html', {'projects':projects})

def detail(request, project_id):
    detailproject = get_object_or_404(Projects, pk=project_id)
    return render(request, 'projects/a.html', {'projects':detailproject})
